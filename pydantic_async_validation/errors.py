class PydanticUserError(Exception):
    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code
        super().__init__(self.message)


class PydanticCustomError(ValueError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
