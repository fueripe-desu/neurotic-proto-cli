from neurotic.parser.command_argument import CommandArgument
from neurotic.parser.command_validator import CommandValidator
from neurotic.parser.main_command import MainCommand
from neurotic.parser.sub_command import SubCommand


class _CommandMapParserError(Exception):
    """Exception raised when the command map parser encounters an error"""

    def __init__(self, message: str):
        self.message: str = message
        super().__init__(self.message)


class CommandMap:
    __has_error: bool = False
    __error_msg: str = ""

    def __init__(self, cmd: list[str]):
        parsed: list[CommandValidator] = self.__parseCmds(cmd)

        if self.__has_error:
            raise _CommandMapParserError(self.__error_msg)

        hash_list: list[int] = []

        for c in parsed:
            hash_list.append(hash(c))

        self.cmd_hash: int = hash(str(hash_list))

    def __parseCmds(self, cmd: list[str]) -> list[CommandValidator]:
        if len(cmd) <= 0:
            self.__setError("At least one command must be specified in map.")
            return []

        main_command: MainCommand = MainCommand(cmd[0])

        if main_command.hasError():
            self.__setError(main_command.error_msg)
            return []

        cmds: list[CommandValidator] = [main_command]

        for c in cmd[1:]:
            if c.startswith("--"):
                if len(cmds) == 0:
                    self.__setError("Command must not start with an argument in map.")

                    return []

                cmd_arg: CommandArgument = CommandArgument(value=c)

                if cmd_arg.hasError():
                    self.__setError(cmd_arg.error_msg)
                    return []

                cmds.append(cmd_arg)
            else:
                if len(cmds) > 0 and type(cmds[-1]) is CommandArgument:
                    self.__setError(
                        "Sub command is not allowed after an argument in map."
                    )
                    return []

                sub_cmd: SubCommand = SubCommand(value=c)

                if sub_cmd.hasError():
                    self.__setError(sub_cmd.error_msg)
                    return []

                cmds.append(SubCommand(value=c))

        return cmds

    def __setError(self, error: str) -> None:
        self.__has_error = True
        self.__error_msg = error
