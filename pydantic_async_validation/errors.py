class PydanticUserError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

class PydanticCustomError(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)