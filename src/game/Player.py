
class Player():
    """Class player for the game"""
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    @property
    def name(self):
        return self._name

    def increase_score(self, score = 1):
        self._score += score

    def reset_score(self):
        self._score = 0

