from neurotic.database.database import Database


def quit_handler(db: Database) -> None:
    _ = db
    exit()
