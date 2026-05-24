from typing import Any


class ConfigParser:
    @staticmethod
    def _loads_file(path: str) -> list[str]:
        with open(path) as config_file:
            return config_file.readlines()

    def parse(
        self, path: str = "maps/easy/01_linear_path.txt"
    ) -> dict[str, Any]:
        for lineno, raw in enumerate(self._loads_file(path), start=1):
            line = raw.split("#")[0].strip()
            if not line:
                continue

            print(f"{lineno}: {line}")

        return {"str": "Any"}
