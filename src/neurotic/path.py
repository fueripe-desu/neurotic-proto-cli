from neurotic.logger import Logger
import pathlib


class Path:
    DATA_DIR_NAME: str = "data"

    def __init__(self, logger: Logger):
        self.__logger = logger
        self.__cwd: pathlib.Path = pathlib.Path.cwd()
        self.__data_dir: pathlib.Path = self.__cwd / self.DATA_DIR_NAME

        self.cwd: str = str(self.__cwd)
        self.data_dir: str = str(self.__data_dir)

        self.__create_dir(self.__data_dir, self.__logger)

    def append_cwd(self, name: str) -> str:
        return str(self.__cwd / name)

    def append_data_dir(self, name: str) -> str:
        return str(self.__data_dir / name)

    def __create_dir(self, path: pathlib.Path, logger: Logger):
        if not path.exists():
            try:
                path.mkdir()
            except FileExistsError:
                logger.critical(f"Directory '{path.name}' already exists.")
            except PermissionError:
                logger.critical(f"Permission denied: Unable to create '{path.name}'.")
            except Exception as e:
                logger.critical(f"An error occurred: {e}")
