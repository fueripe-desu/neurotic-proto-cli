import subprocess


def clear_handler() -> None:
    _ = subprocess.run(["clear"], shell=True)
