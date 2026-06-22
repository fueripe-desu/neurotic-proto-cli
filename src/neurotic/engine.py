from neurotic.prompt import Prompt
from neurotic.logger import Logger

class Engine:
    def __init__(self, prompt: Prompt, logger: Logger):
        self.__prompt = prompt
        self.__logger = logger

        self.__should_close = False

    def close(self) -> None:
        self.__should_close = True

    def run(self):
        while not self.__should_close:
            prompt_value: str = self.__prompt.get_prompt()

            match prompt_value:
                case "clear":
                    os.system("clear")
                case "quit":
                    break
                case _:
                    self.__logger.error(f"Unknown '{prompt_value}' commmand.")

            if (prompt_value == "quit"):
                break

