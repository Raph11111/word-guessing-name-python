from enum import Enum

class Status(Enum):
    CORRECT_POSITION = 1
    WRONG_POSITION = 2
    NOT_FOUND = 3

class GuessEntry:
    def __init__(self,char:str, status: Status)->None:
        if len(char) == 1:
            self.__char = char
            self.__status = status
        else:
            raise ValueError("Wrong size")

    @property
    def char(self)->str:
        return self.__char
    
    @property
    def status(self)->Status:
        return self.__status