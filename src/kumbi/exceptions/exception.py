
class CommandError(Exception):
    """Raise when command is None"""
    def __init__(self, message: str):
        super().__init__(message)