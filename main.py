import sys

from config_parser import ConfigParser


if __name__ == "__main__":
    try:
        config = ConfigParser().parse()
    except FileNotFoundError as e:
        print(f"[ERROR]: File not found — {e.filename}")
        sys.exit(1)
    except PermissionError as e:
        print(f"[ERROR]: Permission denied reading '{e.filename}'")
        sys.exit(1)
