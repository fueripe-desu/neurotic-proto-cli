import logging
import sys
from pathlib import Path


class Logger:
    FILE_LOGGER_NAME: str = "neurotic.file_logger"
    CONSOLE_LOGGER_NAME: str = "neurotic.console_logger"

    def __init__(self):
        self.__file_logger = logging.getLogger(self.FILE_LOGGER_NAME)
        self.__console_logger = logging.getLogger(self.CONSOLE_LOGGER_NAME)

        self.__console_initialized = False
        self.__file_initialized = False

    def configure_console(
        self, level: int = logging.DEBUG, fmt: str = "[%(levelname)s]: %(message)s"
    ) -> None:
        self.__console_logger.setLevel(level)
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logging.Formatter(fmt))

        self.__console_logger.addHandler(consoleHandler)
        self.__console_initialized = True

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
        self.__file_initialized = True

    def __log_console(self, level: int, msg: object) -> None:
        if self.__console_initialized:
            self.__console_logger.log(level, msg)

    def __log_file(self, level: int, msg: object) -> None:
        if self.__file_initialized:
            self.__file_logger.log(level, msg)

    def console_debug(self, msg: object) -> None:
        self.__log_console(logging.DEBUG, msg)

    def console_info(self, msg: object) -> None:
        self.__log_console(logging.INFO, msg)

    def console_warning(self, msg: object) -> None:
        self.__log_console(logging.WARNING, msg)

    def console_error(self, msg: object) -> None:
        self.__log_console(logging.ERROR, msg)

    def console_critical(self, msg: object) -> None:
        self.__log_console(logging.CRITICAL, msg)

    def file_debug(self, msg: object) -> None:
        self.__log_file(logging.DEBUG, msg)

    def file_info(self, msg: object) -> None:
        self.__log_file(logging.INFO, msg)

    def file_warning(self, msg: object) -> None:
        self.__log_file(logging.WARNING, msg)

    def file_error(self, msg: object) -> None:
        self.__log_file(logging.ERROR, msg)

    def file_critical(self, msg: object) -> None:
        self.__log_file(logging.CRITICAL, msg)

    def debug(self, msg: str) -> None:
        self.console_debug(msg)
        self.file_debug(msg)

    def info(self, msg: str) -> None:
        self.console_info(msg)
        self.file_info(msg)

    def warning(self, msg: object) -> None:
        self.console_warning(msg)
        self.file_warning(msg)

    def error(self, msg: object) -> None:
        self.console_error(msg)
        self.file_error(msg)

    def critical(self, msg: object) -> None:
        self.console_critical(msg)
        self.file_critical(msg)
