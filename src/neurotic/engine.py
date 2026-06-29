from neurotic.database.database import Database
from neurotic.logger import Logger
from neurotic.mapper.mapper import Mapper
from neurotic.parser.command import Command
from neurotic.prompt import Prompt


class Engine:
    def __init__(self, mapper: Mapper, prompt: Prompt, db: Database, logger: Logger):
        self.__mapper = mapper
        self.__prompt = prompt
        self.__db = db
        self.__logger = logger

        self.__should_close = False

    def close(self) -> None:
        self.__should_close = True

    def run(self):
        while not self.__should_close:
            prompt_value: Command | None = self.__prompt.get_prompt()

            if prompt_value is None:
                continue

            if not self.__mapper.execute(hash(prompt_value), self.__db):
                self.__logger.error(
                    f"Unknown '{prompt_value.getMainCommandString()}' commmand."
                )
