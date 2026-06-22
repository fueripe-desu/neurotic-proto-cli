from sys import exit
from pathlib import Path
import sqlite3, argparse, os, sys, logging

DATA_DIR_NAME: str = "data"

def create_dir(path: Path, dir_name: str):
    try:
        final_path: Path = path / dir_name;
        final_path.mkdir()
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

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

class Prompt:
    prompt_prefix: str = "$:"

    def __init__(self, prompt_prefix=None):
        if prompt_prefix is not None:
            self.prompt_prefix = prompt_prefix

    def get_prompt(self) -> str:
        return input(f"{self.prompt_prefix} ")

class Engine:
    def __init__(self, prompt: Prompt, logger: Logger):
        self.__prompt = prompt
        self.__logger = logger

        self.__should_close = False

    def close(self) -> None:
        self.__should_close = True

    def run(self):
        while not self.__should_close:
            prompt_value: str = self.__prompt.get_prompt()

            match prompt_value:
                case "clear":
                    os.system("clear")
                case "quit":
                    break
                case _:
                    self.__logger.error(f"Unknown '{prompt_value}' commmand.")

            if (prompt_value == "quit"):
                break

def main():
    parser = argparse.ArgumentParser(description="Neurotic CLI (Prototype)")
    parser.add_argument("--bebel", action="store_true", help="Shows my beloved wife's secret message")

    args = parser.parse_args()

    cwd: Path = Path.cwd()
    data_dir: Path = cwd / DATA_DIR_NAME

    if not data_dir.exists():
        create_dir(cwd, DATA_DIR_NAME)

    logger = Logger(data_dir, "neurotic_cli.log")

    if args.bebel:
        print("My beloved wife's message <3...")
        print("\"Banana\"")
        exit()

    logger.debug("Starting database connection...")
    con: sqlite3.Connection = sqlite3.connect(f"{DATA_DIR_NAME}/neurotic_cli.db")
    logger.info("Connected successfully to the database...")

    engine = Engine(prompt=Prompt(), logger=logger)
    engine.run()

if __name__ == "__main__":
    main()

