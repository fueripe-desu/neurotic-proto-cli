import sys
import pathlib


class Path:
    DATA_DIR_NAME: str = "data"

    def __init__(self):
        self.__cwd: pathlib.Path = pathlib.Path.cwd()
        self.__data_dir: pathlib.Path = self.__cwd / self.DATA_DIR_NAME

        self.cwd: str = str(self.__cwd)
        self.data_dir: str = str(self.__data_dir)

        self.__create_dir(self.__data_dir)

    def append_cwd(self, name: str) -> str:
        return str(self.__cwd / name)

    def append_data_dir(self, name: str) -> str:
        return str(self.__data_dir / name)

    def __create_dir(self, path: pathlib.Path):
        if not path.exists():
            try:
                path.mkdir()
            except FileExistsError:
                _ = sys.stderr.write(f"Directory '{path.name}' already exists.\n")
                _ = sys.stderr.flush()
            except PermissionError:
                _ = sys.stderr.write(
                    f"Permission denied: Unable to create '{path.name}'."
                )
                _ = sys.stderr.flush()
            except Exception as e:
                _ = sys.stderr.write(f"An error occurred: {e}")
                _ = sys.stderr.flush()
