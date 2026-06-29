from typing import Callable
from neurotic.database.database import Database
from neurotic.mapper.command_map import CommandMap


class _DuplicateCommandError(Exception):
    """Exception raised when the same command map has been registered twice."""

    def __init__(self):
        super().__init__("Command has been registered twice.")


class Mapper:
    __cmd_map: dict[int, Callable[[Database], None]] = {}

    def register_cmd(
        self, cmd_map: CommandMap, handler: Callable[[Database], None]
    ) -> None:
        if self.__cmd_map.get(cmd_map.cmd_hash) is not None:
            raise _DuplicateCommandError()

        self.__cmd_map[cmd_map.cmd_hash] = handler

    def execute(self, cmd_hash: int, db: Database) -> bool:
        handler = self.__cmd_map.get(cmd_hash)

        if handler is None:
            return False

        self.__cmd_map[cmd_hash](db)
        return True
