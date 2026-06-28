from neurotic.parser.command_validator import CommandValidator


class SubCommand(CommandValidator):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.__value = value

        if self.__value.startswith("-") or self.__value.endswith("-"):
            return self.setError("Sub command must not start or end with dashes.")
