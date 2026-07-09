"""
AI formatter service (OpenRouter, free models with automatic rotation).

Turns messy admission / entry-requirements text into a clean, categorised HTML
table so it renders nicely once stored in the DB. Provider-neutral by design —
everything OpenRouter-specific is contained in this one file.

Design:
  * Uses OpenRouter's OpenAI-compatible chat endpoint.
  * Discovers the currently-available FREE models live from /api/v1/models and
    rotates through them: when one is rate-limited / exhausted (HTTP 402/429),
    the next free model is tried automatically.
  * The model returns STRICT JSON (categories + bullet details); Python renders
    the <table> deterministically, so the DB never gets malformed HTML.
  * Disk cache keyed by a hash of the input — re-running a scraper does NOT
    re-bill the API (and free models have daily limits).
  * Opt-in: disabled unless OPENROUTER_API_KEY is set (or LLM_FORMAT=1). Scrapers
    fall back to their normal HTML when it's off or the call fails, so nothing
    breaks without a key.

Enable:   set OPENROUTER_API_KEY=sk-or-...   (optionally LLM_FORMAT=1)
"""
import os
import re
import json
import hashlib
import urllib.request
import urllib.error

OPENROUTER_URL = "https://openrouter.ai/api/v1"
_ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(_ROOT, ".ai_format_cache.json")


# ---------- load OPENROUTER_API_KEY from a local .env (no dependency) ----------
def _load_dotenv():
    path = os.path.join(_ROOT, ".env")
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and k not in os.environ:
                    os.environ[k] = v
    except FileNotFoundError:
        pass
    except Exception:
        pass

_load_dotenv()

# Preferred free models (tried first, in order); any other :free model discovered
# from the API is appended after these as extra fallbacks.
PREFERRED_FREE = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "openai/gpt-oss-120b:free",
    "google/gemma-4-31b-it:free",
    "nousresearch/hermes-3-llama-3.1-405b:free",
    "openrouter/free",
]

SYSTEM_PROMPT = (
    "You reformat a course's Entry Requirements into a clean, categorised structure "
    "so it is easy to read in a table. You ONLY reorganise the text you are given. "
    "Do NOT add, invent, infer, translate, or embellish anything — if a detail is not "
    "in the text, do not include it. Group the requirements into sensible categories "
    "such as: Age, Academic Requirements, English Proficiency, Language/Literacy/Numeracy (LLND), "
    "Student Equipment, Interview, Other. Keep each detail concise and faithful to the source. "
    'Return STRICT JSON only, no markdown, in this exact shape: '
    '{"rows":[{"category":"<label>","details":["<point>","<point>"]}]}'
)

_MODELS_CACHE = None       # discovered free-model order
_MODEL_IDX = 0             # rotation cursor
_DISK_CACHE = None


# ---------- enable / cache ----------
def _api_key():
    return os.environ.get("OPENROUTER_API_KEY", "").strip()

def enabled():
    if not _api_key():
        return False
    flag = os.environ.get("LLM_FORMAT", "1").strip().lower()
    return flag in ("1", "true", "yes")

def _load_cache():
    global _DISK_CACHE
    if _DISK_CACHE is None:
        try:
            with open(CACHE_PATH, encoding="utf-8") as f:
                _DISK_CACHE = json.load(f)
        except Exception:
            _DISK_CACHE = {}
    return _DISK_CACHE

def _save_cache():
    try:
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(_DISK_CACHE, f, ensure_ascii=False)
    except Exception:
        pass


# ---------- model discovery + rotation ----------
def _free_models():
    global _MODELS_CACHE
    if _MODELS_CACHE is not None:
        return _MODELS_CACHE
    discovered = []
    try:
        req = urllib.request.Request(f"{OPENROUTER_URL}/models", headers={"User-Agent": "course-scraper"})
        data = json.loads(urllib.request.urlopen(req, timeout=30).read().decode("utf-8"))
        for m in data.get("data", []):
            p = m.get("pricing", {})
            if str(p.get("prompt", "1")) in ("0", "0.0") and str(p.get("completion", "1")) in ("0", "0.0"):
                mid = m.get("id")
                # skip obvious non-text models
                if mid and not any(x in mid for x in ("lyria", "content-safety", "-vl", "-omni")):
                    discovered.append(mid)
    except Exception:
        pass
    ordered = [m for m in PREFERRED_FREE if m in discovered] or list(PREFERRED_FREE)
    ordered += [m for m in discovered if m not in ordered]
    _MODELS_CACHE = ordered
    return ordered


def _chat(text):
    """Try free models in rotation order; return assistant content or None."""
    global _MODEL_IDX
    models = _free_models()
    if not models:
        return None
    body = {
        "models": None,  # set per-attempt below
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        "temperature": 0,
        "max_tokens": 1200,
    }
    headers = {
        "Authorization": f"Bearer {_api_key()}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/devinterlacebali/WebScraping-CourseCricos",
        "X-Title": "Course Scraper Formatter",
    }
    attempts = len(models)
    for _ in range(attempts):
        model = models[_MODEL_IDX % len(models)]
        payload = dict(body)
        payload.pop("models", None)
        payload["model"] = model
        req = urllib.request.Request(
            f"{OPENROUTER_URL}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            resp = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
            content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
            if content and content.strip():
                return content
            _MODEL_IDX += 1  # empty answer -> rotate
        except urllib.error.HTTPError as e:
            # 402/429 = quota/rate exhausted -> rotate to next free model
            if e.code in (402, 429, 403, 500, 502, 503):
                _MODEL_IDX += 1
                continue
            _MODEL_IDX += 1
        except Exception:
            _MODEL_IDX += 1
    return None


# ---------- JSON parsing + HTML rendering ----------
def _extract_json(s):
    s = re.sub(r"^```(?:json)?|```$", "", s.strip(), flags=re.MULTILINE).strip()
    m = re.search(r"\{.*\}", s, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

def _render_table(obj):
    rows = obj.get("rows") if isinstance(obj, dict) else None
    if not rows:
        return ""
    out = ["<table><tbody>"]
    for r in rows:
        cat = str(r.get("category", "")).strip()
        details = r.get("details") or []
        if isinstance(details, str):
            details = [details]
        details = [str(d).strip() for d in details if str(d).strip()]
        if not cat and not details:
            continue
        if len(details) == 1:
            cell = details[0]
        else:
            cell = "<ul>" + "".join(f"<li>{d}</li>" for d in details) + "</ul>"
        out.append(f"<tr><td><strong>{cat}</strong></td><td>{cell}</td></tr>")
    out.append("</tbody></table>")
    return "".join(out)


# ---------- public API ----------
def format_requirements(plain_text):
    """Return a categorised HTML <table> for the given requirements text, or ""."""
    text = re.sub(r"\s+", " ", (plain_text or "")).strip()
    if not enabled() or len(text) < 40:
        return ""
    key = hashlib.sha256(text.encode("utf-8")).hexdigest()
    cache = _load_cache()
    if key in cache:
        return cache[key]

    content = _chat(text)
    table = ""
    if content:
        obj = _extract_json(content)
        if obj:
            table = _render_table(obj)

    cache[key] = table  # cache even "" to avoid re-calling on the same failing input
    _save_cache()
    return table
