class ConfigReader:
    def __init__(
        self, file_path: str = "maps/easy/01_linear_path.txt"
    ) -> None:
        self.file_path: str = file_path

    def loads(self) -> list[str]:
        with open(self.file_path) as config_file:
            return config_file.readlines()
