from sys import exit
import sqlite3
import argparse
from neurotic.handlers.clear_handler import clear_handler
from neurotic.handlers.quit_handler import quit_handler
from neurotic.logger import Logger
from neurotic.engine import Engine
from neurotic.mapper.command_map import CommandMap
from neurotic.mapper.mapper import Mapper
from neurotic.prompt import Prompt
from neurotic.path import Path


def example() -> None:
    print("Example")


def main():
    path = Path()
    logger = Logger(path, "neurotic_cli.log")

    parser = argparse.ArgumentParser(description="Neurotic CLI (Prototype)")
    _ = parser.add_argument(
        "--bebel", action="store_true", help="Shows my beloved wife's secret message"
    )

    args = parser.parse_args()

    if args.bebel:  # pyright: ignore[reportAny]
        print("My beloved wife's message <3...")
        print('"Banana"')
        exit()

    logger.debug("Starting database connection...")
    con: sqlite3.Connection = sqlite3.connect(f"{path.DATA_DIR_NAME}/neurotic_cli.db")
    logger.info("Connected successfully to the database...")

    mapper: Mapper = Mapper()

    mapper.register_cmd(
        cmd_map=CommandMap(["quit"]),
        handler=quit_handler,
    )

    mapper.register_cmd(
        cmd_map=CommandMap(["clear"]),
        handler=clear_handler,
    )

    engine = Engine(mapper=mapper, prompt=Prompt(logger), logger=logger)
    engine.run()


if __name__ == "__main__":
    main()
