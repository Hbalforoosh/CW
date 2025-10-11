class InsufficientCredit(Exception):
    def __init__(self, message="Not enough credit") -> None:
        super().__init__(message)
