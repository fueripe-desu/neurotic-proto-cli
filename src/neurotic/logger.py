from pathlib import Path
import sys, logging

class Logger:
    def __init__(self, path: Path, filename: str):
        self.__file_logger = logging.getLogger("neurotic.file_logger")
        self.__console_logger = logging.getLogger("neurotic.console_logger")

        self.__file_logger.setLevel(logging.DEBUG)
        self.__console_logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler(path / filename)
        fileHandler.setFormatter(logging.Formatter(
            fmt= "%(asctime)s [%(levelname)s]: %(message)s"
        ))

        self.__file_logger.addHandler(fileHandler)

        console_formatter = logging.Formatter(
            fmt= "[%(levelname)s]: %(message)s"
        )

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(console_formatter)

        self.__console_logger.addHandler(consoleHandler)

    def debug(self, msg: str) -> None:
        self.__file_logger.debug(msg)
        self.__console_logger.debug(msg)

    def info(self, msg: str) -> None:
        self.__file_logger.info(msg)
        self.__console_logger.info(msg)

    def warning(self, msg: object) -> None:
        self.__file_logger.warning(msg)
        self.__console_logger.warning(msg)

    def error(self, msg: object) -> None:
        self.__file_logger.error(msg)
        self.__console_logger.error(msg)

    def critical(self, msg: object) -> None:
        self.__file_logger.critical(msg)
        self.__console_logger.critical(msg)

