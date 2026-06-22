from sys import exit
from pathlib import Path
import sqlite3, argparse
from neurotic.logger import Logger
from neurotic.engine import Engine
from neurotic.prompt import Prompt

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

