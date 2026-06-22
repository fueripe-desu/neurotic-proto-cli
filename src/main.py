from sys import exit
from pathlib import Path
import sqlite3, argparse, os

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

class Prompt:
    prompt_prefix: str = "$:"

    def __init__(self, prompt_prefix=None):
        if prompt_prefix is not None:
            self.prompt_prefix = prompt_prefix

    def get_prompt(self) -> str:
        return input(f"{self.prompt_prefix} ")

class Engine:
    def __init__(self, prompt: Prompt):
        self.__prompt = prompt
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
                    print(f"[Error]: Unknown '{prompt_value}' commmand.")

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

    if args.bebel:
        print("My beloved wife's message <3...")
        print("\"Banana\"")
        exit()

    con: sqlite3.Connection = sqlite3.connect(f"{DATA_DIR_NAME}/neurotic_cli.db")

    engine = Engine(prompt=Prompt())
    engine.run()

if __name__ == "__main__":
    main()

