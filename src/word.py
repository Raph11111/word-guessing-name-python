from typing import Dict, Union, List

class Word:
    __WORD_LENGTH: int = 5

    __word : Dict[str, Union[int,List[int]]]
    __original_word: str

    def __init__(self, word: str) -> None:
        if len(word) != self.__WORD_LENGTH:
            raise ValueError("Wrong size")
        if not word.isalpha():
            raise ValueError("Wrong type")
        self.__original_word = word
        
        temp_word_data: Dict[str, List[int]] = {}
        for i, char in enumerate(word):
            upper_char = char.upper()
            if upper_char not in temp_word_data:
                temp_word_data[upper_char] = []
            temp_word_data[upper_char].append(i + 1)

        self.__word = {}
        for char in sorted(temp_word_data.keys()):
            positions = temp_word_data[char]
            if len(positions) == 1:
                self.__word[char] = positions[0]
            else:
                self.__word[char] = sorted(positions)


    def __str__(self) -> str:
        return self.__original_word.upper()

    @classmethod
    def get_word_length(cls) -> int:
        return cls.__WORD_LENGTH

    @property
    def word(self)->Dict[str, Union[int, List[int]]]:
        return self.__word.copy()