from sys import exit
import sqlite3
import argparse
from neurotic.logger import Logger
from neurotic.engine import Engine
from neurotic.prompt import Prompt
from neurotic.path import Path


def main():
    logger = Logger()
    logger.configure_console()

    path = Path(logger=logger)

    parser = argparse.ArgumentParser(description="Neurotic CLI (Prototype)")
    _ = parser.add_argument(
        "--bebel", action="store_true", help="Shows my beloved wife's secret message"
    )

    args = parser.parse_args()

    logger_file_path = path.append_data_dir("neurotic_cli.log")
    logger.configure_file(logger_file_path)

    if args.bebel:  # pyright: ignore[reportAny]
        print("My beloved wife's message <3...")
        print('"Banana"')
        exit()

    logger.debug("Starting database connection...")
    con: sqlite3.Connection = sqlite3.connect(f"{path.DATA_DIR_NAME}/neurotic_cli.db")
    logger.info("Connected successfully to the database...")

    engine = Engine(prompt=Prompt(), logger=logger)
    engine.run()


if __name__ == "__main__":
    main()
