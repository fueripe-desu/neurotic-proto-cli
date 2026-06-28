class CommandValidator:
    error_msg: str = ""
    __has_error: bool = False

    def setError(self, error: str) -> None:
        self.error_msg = error
        self.__has_error = True

    def hasError(self) -> bool:
        return self.__has_error
