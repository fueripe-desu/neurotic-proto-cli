from typing import override

from neurotic.parser.command_argument import CommandArgument
from neurotic.parser.command_validator import CommandValidator
from neurotic.parser.main_command import MainCommand
from neurotic.parser.sub_command import SubCommand


class Command:
    __has_error: bool = False
    __error_msg: str = ""

    def __init__(self, prompt: str) -> None:
        self.cmds: list[CommandValidator] = []
        splitted: list[str] = prompt.split()

        if len(splitted) == 0:
            return

        main_command: MainCommand = MainCommand(value=splitted[0])

        if main_command.hasError():
            self.__setError(main_command.error_msg)
            return

        self.cmds = [main_command]

        for c in splitted[1:]:
            if c.startswith("--"):
                if len(self.cmds) == 0:
                    return self.__setError("Command must not start with an argument.")

                cmd_arg: CommandArgument = CommandArgument(value=c)

                if cmd_arg.hasError():
                    return self.__setError(cmd_arg.error_msg)

                self.cmds.append(cmd_arg)
            else:
                if len(self.cmds) > 0 and type(self.cmds[-1]) is CommandArgument:
                    return self.__setError(
                        "Sub command is not allowed after an argument."
                    )

                sub_cmd: SubCommand = SubCommand(value=c)

                if sub_cmd.hasError():
                    return self.__setError(sub_cmd.error_msg)

                self.cmds.append(SubCommand(value=c))

    def isEmpty(self) -> bool:
        return len(self.cmds) == 0

    def hasError(self) -> bool:
        return self.__has_error

    def getErrorMessage(self) -> str:
        return self.__error_msg

    def __setError(self, error: str):
        self.__has_error = True
        self.__error_msg = error

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Command):
            return False

        return self.cmds == other.cmds

    @override
    def __hash__(self) -> int:
        hash_list: list[int] = []

        for c in self.cmds:
            hash_list.append(hash(c))

        return hash(str(hash_list))
