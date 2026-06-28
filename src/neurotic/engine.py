import subprocess

from neurotic.logger import Logger
from neurotic.parser.command import Command
from neurotic.prompt import Prompt


class Engine:
    def __init__(self, prompt: Prompt, logger: Logger):
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

            print(hash(prompt_value))

            # match prompt_value:
            #     case "clear":
            #         _ = subprocess.run(["clear"], shell=True)
            #     case "quit":
            #         break
            #     case _:
            #         self.__logger.error(f"Unknown '{prompt_value}' commmand.")

            # if prompt_value == "quit":
            #     break
