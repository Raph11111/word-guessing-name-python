from name import Name
from score import Score

class Player:
    def __init__(self, name: str = None):
        self.__name = Name(name)  # Name mit optionalem Parameter
        self.__score = Score()

    def reset(self) -> None:
        self.__score.reset()

    @property
    def name(self) -> Name:
        return self.__name

    @property
    def score(self) -> Score:
        return self.__score