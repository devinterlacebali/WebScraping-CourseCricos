import os

# Intercept Playwright browser launch to override headless mode
try:
    from playwright._impl._browser_type import BrowserType
    original_launch = BrowserType.launch

    def custom_launch(self, *args, **kwargs):
        headless_env = os.environ.get("SCRAPER_HEADLESS")
        if headless_env is not None:
            kwargs["headless"] = (headless_env.lower() == "true")
        return original_launch(self, *args, **kwargs)

    BrowserType.launch = custom_launch
except Exception:
    # Fail-safe: do nothing if playwright is not installed or import structure changes
    pass
