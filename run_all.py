import os
import subprocess
import sys
import re
import time

# Force UTF-8 encoding for stdout and stderr on Windows to support emojis in console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# List of folder/file name patterns to exclude (test scripts, utilities, etc.)
EXCLUDE_PATTERNS = [
    r"test",
    r"clean",
    r"merge",
    r"coba",
    r"filter",
    r"get_link",
    r"fee",
    r"venv",
    r"\.git"
]

# Error and Warning patterns in logs
FATAL_ERR_PATTERNS = [
    r"modulenotfounderror",
    r"filenotfounderror",
    r"syntaxerror",
    r"traceback",
    r"exception",
    r"attributeerror",
    r"nameerror",
    r"keyerror",
    r"indexerror",
    r"can't open file",
    r"no such file or directory",
    r"invalid syntax",
    r"connectionerror",
    r"403 forbidden",
    r"empty body"
]

WARNING_PATTERNS = [
    r"timeout",
    r"gagal buka",
    r"skip",
    r"not found",
    r"unknown",
    r"retry",
    r"error at"
]

def should_exclude(path):
    path_lower = path.lower().replace("\\", "/")
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, path_lower):
            return True
    return False

def find_scrapers(root_dir):
    scrapers = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not should_exclude(d)]
        for file in files:
            if file.endswith(".py") and not should_exclude(file):
                full_path = os.path.join(root, file)
                # Exclude scripts directly in the root directory (like run_all.py or sitecustomize.py)
                if os.path.abspath(root) == os.path.abspath(root_dir):
                    continue
                scrapers.append(full_path)
    return sorted(scrapers)

def determine_cwd_and_args(script_path, root_dir):
    script_dir = os.path.dirname(script_path)
    dir_name = os.path.basename(script_dir)
    
    try:
        with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        content = ""

    if dir_name in content:
        return root_dir, script_path
    else:
        return script_dir, os.path.basename(script_path)

def analyze_logs(logs, exit_code):
    has_fatal = False
    has_warning = False
    fatal_matches = []
    warning_matches = []

    if exit_code != 0:
        has_fatal = True
        fatal_matches.append(f"Exit code {exit_code}")

    for line in logs:
        line_lower = line.lower()
        # Check fatals
        for pat in FATAL_ERR_PATTERNS:
            if re.search(pat, line_lower):
                has_fatal = True
                fatal_matches.append(line.strip())
                break
        
        # Check warnings
        for pat in WARNING_PATTERNS:
            if re.search(pat, line_lower):
                has_warning = True
                warning_matches.append(line.strip())
                break

    # Deduplicate matches
    fatal_matches = list(set(fatal_matches))[:3]
    warning_matches = list(set(warning_matches))[:3]

    if has_fatal:
        return "🔴 BROKEN (RUSAK)", fatal_matches
    elif has_warning:
        return "🟡 WARNING (PERINGATAN)", warning_matches
    else:
        return "🟢 HEALTHY (SEHAT)", []

def main():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    scrapers = find_scrapers(root_dir)

    if not scrapers:
        print("❌ No scraper scripts found!")
        sys.exit(1)

    print("====================================================")
    print(f"🔍 Found {len(scrapers)} scraper scripts:")
    print("====================================================")
    for idx, s in enumerate(scrapers, 1):
        rel_path = os.path.relpath(s, root_dir)
        print(f"[{idx}] {rel_path}")
    print("====================================================\n")

    print("Select run mode:")
    print("  'all'  - Run all scrapers in sequence and analyze health")
    print("  '1,3'  - Run specific scrapers by indices (comma-separated)")
    print("  'q'    - Quit")
    choice = input("\nYour choice: ").strip().lower()

    if choice == 'q':
        print("Bye!")
        sys.exit(0)

    selected_scrapers = []
    if choice == 'all':
        selected_scrapers = scrapers
    else:
        try:
            indices = [int(x.strip()) for x in choice.split(",") if x.strip()]
            for idx in indices:
                if 1 <= idx <= len(scrapers):
                    selected_scrapers.append(scrapers[idx - 1])
                else:
                    print(f"⚠️ Index {idx} out of range, skipping.")
        except ValueError:
            print("❌ Invalid input! Please enter 'all', 'q', or a comma-separated list of numbers.")
            sys.exit(1)

    if not selected_scrapers:
        print("❌ No scrapers selected. Exiting.")
        sys.exit(0)

    # Prompt for Headed vs Headless mode
    headed_choice = input("\nDo you want to run in headed mode (visible browser window)? / Ingin jalankan dengan tampilan browser? [y/N]: ").strip().lower()
    headless_val = "False" if headed_choice in ("y", "yes") else "True"

    print(f"\n🚀 Running {len(selected_scrapers)} scrapers (Headless={headless_val}) and analyzing health...")
    results = []

    for idx, s in enumerate(selected_scrapers, 1):
        rel_path = os.path.relpath(s, root_dir)
        cwd, run_target = determine_cwd_and_args(s, root_dir)
        
        print("\n" + "="*60)
        print(f"[{idx}/{len(selected_scrapers)}] RUNNING: {rel_path}")
        print(f"Working Directory: {os.path.relpath(cwd, root_dir) or '.'}")
        print(f"Command: python {run_target}")
        print("="*60 + "\n")
        sys.stdout.flush()

        logs = []
        exit_code = 0
        try:
            # Prepare environment variables to inject monkeypatch and force UTF-8 output
            env = os.environ.copy()
            env["SCRAPER_HEADLESS"] = headless_val
            env["PYTHONPATH"] = root_dir
            env["PYTHONIOENCODING"] = "utf-8"
            env["PYTHONUNBUFFERED"] = "1"
            
            # Use -u to force unbuffered output in python subprocesses
            cmd = [sys.executable, "-u", run_target]
            
            process = subprocess.Popen(
                cmd,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
                env=env
            )
            
            # Print output in real-time and capture logs
            for line in process.stdout:
                print(line, end="")
                sys.stdout.flush()
                logs.append(line)
                
            process.wait()
            exit_code = process.returncode
        except Exception as e:
            err_msg = str(e)
            print(f"\n❌ ERROR running {rel_path}: {err_msg}")
            logs.append(f"EXCEPTION: {err_msg}")
            exit_code = -1

        status, matches = analyze_logs(logs, exit_code)
        results.append({
            "name": rel_path,
            "status": status,
            "details": matches
        })
        print(f"\nHealth Check Result: {status}")


    print("\n" + "="*60)
    print("📊 SCRAPER HEALTH SUMMARY REPORT")
    print("="*60)
    
    # Group results
    healthy = [r for r in results if "HEALTHY" in r["status"]]
    warning = [r for r in results if "WARNING" in r["status"]]
    broken = [r for r in results if "BROKEN" in r["status"]]

    print(f"🟢 HEALTHY (SEHAT):      {len(healthy)}")
    print(f"🟡 WARNING (PERINGATAN):  {len(warning)}")
    print(f"🔴 BROKEN (RUSAK):        {len(broken)}")
    print("-" * 60)

    if broken:
        print("\n🔴 BROKEN SCRAPERS (Action Required):")
        for b in broken:
            print(f"  • {b['name']}")
            if b['details']:
                print(f"    Reason(s):")
                for d in b['details']:
                    print(f"      - {d}")

    if warning:
        print("\n🟡 WARNING SCRAPERS (Check Logs):")
        for w in warning:
            print(f"  • {w['name']}")
            if w['details']:
                print(f"    Detail(s):")
                for d in w['details']:
                    print(f"      - {d}")

    if healthy:
        print("\n🟢 HEALTHY SCRAPERS:")
        for h in healthy:
            print(f"  • {h['name']}")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
