from enum import Enum
import re
from typing import override

from neurotic.parser.command_validator import CommandValidator


class _ParserState(Enum):
    KEY = 1
    VALUE = 2
    END = 3


class CommandArgument(CommandValidator):
    __arg_charset: re.Pattern[str] = re.compile("^[a-z-]$")

    def __init__(self, value: str) -> None:
        super().__init__()

        self.__key: list[str] = []
        self.__value: list[str] = []

        dash_count: int = 0
        state: _ParserState = _ParserState.KEY

        for c in value:
            if state == _ParserState.KEY:
                if c == "-" and len(self.__key) == 0:
                    dash_count += 1
                elif c == "=":
                    state = _ParserState.VALUE

                    if self.__key[-1] == "-":
                        return self.setError("Argument key must not end in a dash.")

                elif not c.isalpha() and not c.islower() and not c == "-":
                    return self.setError(
                        "Argument key must only contain alphabetic characters and be separated by dashes."
                    )

                else:
                    self.__key.append(c)
            else:
                if c == " " and len(self.__key) == 0:
                    continue
                elif c != '"' and len(self.__key) == 0:
                    return self.setError(
                        "Argument value must start with double quotes."
                    )
                elif c == '"' and len(self.__key) == 0:
                    continue
                elif c == '"' and len(self.__key) > 0:
                    state = _ParserState.END
                else:
                    self.__value.append(c)

        if dash_count != 2:
            return self.setError(
                "Argument key must not start with more than two dashes."
            )

        self.__key_str = "".join(self.__key)
        self.__value_str = "".join(self.__value)

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CommandArgument):
            return False

        return self.__key_str == other.__key_str

    @override
    def __hash__(self) -> int:
        return hash(self.__key_str)
