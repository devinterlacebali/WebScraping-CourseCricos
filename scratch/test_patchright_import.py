import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("Trying to import patchright...")
    try:
        import patchright
        print("Successfully imported patchright!")
        print("Directory of patchright:", dir(patchright))
    except Exception as e:
        print("Error importing patchright:", e)

if __name__ == "__main__":
    main()
