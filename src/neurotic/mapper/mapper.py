from typing import Callable
from neurotic.mapper.command_map import CommandMap


class Mapper:
    __cmd_map: dict[int, Callable[[], None]] = {}

    def register_cmd(self, cmd_map: CommandMap, handler: Callable[[], None]):
        print(cmd_map.cmd_hash)
        self.__cmd_map[cmd_map.cmd_hash] = handler

    def execute(self, cmd_hash: int) -> None:
        self.__cmd_map[cmd_hash]()
