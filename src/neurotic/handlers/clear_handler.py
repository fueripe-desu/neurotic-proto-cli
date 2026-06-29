import subprocess

from neurotic.database.database import Database


def clear_handler(db: Database) -> None:
    _ = db
    _ = subprocess.run(["clear"], shell=True)
