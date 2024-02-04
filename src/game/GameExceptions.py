class GameException(Exception):
    "Raised when there is an exception with the 'Game'"
    pass

class NoPlayersException(GameException):
    "Raised when trying to make a 'Game' without players"
    def __init__(self, message = "The number of players must be at least of 1"):            
        super().__init__(message)
