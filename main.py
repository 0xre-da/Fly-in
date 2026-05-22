import sys

from config_reader import ConfigReader


if __name__ == "__main__":
    config_reader = ConfigReader()
    try:
        config = config_reader.loads()
    except FileNotFoundError as e:
        print(f"[ERROR]: File not found — {e.filename}")
        sys.exit(1)
    except PermissionError as e:
        print(f"[ERROR]: Permission denied reading '{e.filename}'")
        sys.exit(1)
