class Prompt:
    prompt_prefix: str = "$:"

    def __init__(self, prompt_prefix: str | None = None):
        if prompt_prefix is not None:
            self.prompt_prefix = prompt_prefix

    def get_prompt(self) -> str:
        return input(f"{self.prompt_prefix} ")
