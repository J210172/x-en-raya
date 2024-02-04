from GameExceptions import NoPlayersException

class Game():
    """The actual game"""

    def __init__(self, num_players = 2):
        if num_players < 1:
            raise NoPlayersException()
        self._num_players = num_players
        self._players = ()
        self._turn = 0
        self.init_players()

    def init_players(self):
        self._players = (p for p in range(self.num))

    @property
    def num_players(self):
        return self._num_players
    
    def next_turn(self):
        self._turn += 1
