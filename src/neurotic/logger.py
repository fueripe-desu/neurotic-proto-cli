import logging
import sys
from pathlib import Path


class Logger:
    FILE_LOGGER_NAME: str = "neurotic.file_logger"
    CONSOLE_LOGGER_NAME: str = "neurotic.console_logger"

    def __init__(self):
        self.__file_logger = logging.getLogger(self.FILE_LOGGER_NAME)
        self.__console_logger = logging.getLogger(self.CONSOLE_LOGGER_NAME)

    def configure_console(
        self, level: int = logging.DEBUG, fmt: str = "[%(levelname)s]: %(message)s"
    ) -> None:
        self.__console_logger.setLevel(level)
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logging.Formatter(fmt))

        self.__console_logger.addHandler(consoleHandler)

    def configure_file(
        self,
        path: Path,
        filename: str,
        level: int = logging.DEBUG,
        fmt: str = "%(asctime)s [%(levelname)s]: %(message)s",
    ) -> None:
        self.__file_logger.setLevel(level)
        fileHandler = logging.FileHandler(path / filename)
        fileHandler.setFormatter(logging.Formatter(fmt))

        self.__file_logger.addHandler(fileHandler)

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
