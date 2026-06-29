import sqlite3

from neurotic.path import Path


class Database:
    DEFAULT_DB_NAME: str = "neurotic_cli.db"

    def __init__(self, path: Path):
        self.__con: sqlite3.Connection = sqlite3.connect(
            f"{path.DATA_DIR_NAME}/{self.DEFAULT_DB_NAME}"
        )
