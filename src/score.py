class Score:
    def __init__(self)->None:
        self.__points = 0
    def add(self,points:int)->None:
        self.__points += points
    def reset(self)->None:
        self.__points = 0
    @property
    def points(self)->int:
        return self.__points
