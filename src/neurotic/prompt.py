from neurotic.logger import Logger
from neurotic.parser.command import Command


class Prompt:
    prompt_prefix: str = "$:"

    def __init__(self, logger: Logger, prompt_prefix: str | None = None):
        self.__logger = logger

        if prompt_prefix is not None:
            self.prompt_prefix = prompt_prefix

    def get_prompt(self) -> Command | None:
        prompt_value = input(f"{self.prompt_prefix} ")

        cmd: Command = Command(prompt_value)

        if cmd.hasError():
            self.__logger.error(cmd.getErrorMessage())
            return

        if cmd.isEmpty():
            return

        return cmd
