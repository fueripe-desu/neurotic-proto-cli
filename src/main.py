from pathlib import Path
import sqlite3

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
    print("Starting database connection...")

    cwd: Path = Path.cwd()
    data_dir: Path = cwd / DATA_DIR_NAME

    if not data_dir.exists():
        create_dir(cwd, DATA_DIR_NAME)

    con: sqlite3.Connection = sqlite3.connect("data/neurotic_cli.db")

if __name__ == "__main__":
    main()

