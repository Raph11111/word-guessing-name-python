from word import Word
import json
import random
from word_list_factory import WordListFactory
class WordListFromJsonFile(WordListFactory):
    def __init__(self, file_path:str)->None:
        self.__word_list = self.__load_word_list(file_path)

    def get_word(self, index:int)->Word:
        try:
            return self.__word_list[index]
        except IndexError:
            raise IndexError("Index out of range")

    def get_number_of_words(self)->int:
        return len(self.__word_list)

    def __load_word_list(self,file_path: str)->list[Word]:
        word_list = []
        try:
            with open(file_path, 'r',encoding='utf-8') as file:
                data = json.load(file)
                for i in range(len(data)):
                    if data[i]['word'].isalpha():
                        word_list.append(self._json_to_word(data[i]))
                    elif not data[i]['word'].isalpha():
                        for char in data[i]['word']:
                            if char.isdigit():
                                raise ValueError("Word must contain only alphabetic characters.")
                    
                
                random.shuffle(word_list)
                return word_list
        except FileNotFoundError:
            raise
        except json.JSONDecodeError as e:
            raise Exception("tmp_invalid.json")

    def _json_to_word(self,json_dict : dict)->Word:
        return Word(json_dict['word'])



        
            
    