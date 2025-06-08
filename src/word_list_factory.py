from abc import ABC, abstractmethod
from word import Word
class WordListFactory(ABC):
    @abstractmethod
    def get_number_of_words(self)->int:
        pass

    @abstractmethod
    def get_word(self,index:int)->Word:
        pass

    def _json_to_word(self,json_dict: dict)->Word:
        return Word(json_dict['word'])