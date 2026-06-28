from typing import override
from neurotic.parser.command_validator import CommandValidator


class SubCommand(CommandValidator):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.__value = value

        if self.__value.startswith("-") or self.__value.endswith("-"):
            return self.setError("Sub command must not start or end with dashes.")

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SubCommand):
            return False

        return self.__value == other.__value

    @override
    def __hash__(self) -> int:
        return hash(self.__value)
