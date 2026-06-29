import subprocess

from neurotic.logger import Logger
from neurotic.mapper.mapper import Mapper
from neurotic.parser.command import Command
from neurotic.prompt import Prompt


class Engine:
    def __init__(self, mapper: Mapper, prompt: Prompt, logger: Logger):
        self.__mapper = mapper
        self.__prompt = prompt
        self.__logger = logger

        self.__should_close = False

    def close(self) -> None:
        self.__should_close = True

    def run(self):
        while not self.__should_close:
            prompt_value: Command | None = self.__prompt.get_prompt()

            if prompt_value is None:
                continue

            if not self.__mapper.execute(hash(prompt_value)):
                self.__logger.error(
                    f"Unknown '{prompt_value.getMainCommandString()}' commmand."
                )

            # match prompt_value:
            #     case "clear":
            #         _ = subprocess.run(["clear"], shell=True)
            #     case "quit":
            #         break
            #     case _:
            #         self.__logger.error(f"Unknown '{prompt_value}' commmand.")

            # if prompt_value == "quit":
            #     break
