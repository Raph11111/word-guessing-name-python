import sys 
from guess_entry import Status, GuessEntry
from guess_history import GuessHistory
from word import Word


class Guess:

    MAX_ATTEMPTS: int = 6 # Static member as per UML

    def __init__(self, solution: Word) -> None:
        if not isinstance(solution, Word):
            raise TypeError("Solution must be an instance of Word.")
        self.__solution: Word = solution
        self.__number_of_attempts: int = 0
        # The word length is now retrieved using Word.get_word_length()
        self.__guess_history: GuessHistory = GuessHistory(self.MAX_ATTEMPTS, Word.get_word_length())
        

    def _query_user_input(self) -> str:
        word_length = Word.get_word_length() 
        while True:
            try:
                user_input = input("Enter your guess: ").strip().upper()
                if len(user_input) != word_length:
                    print(f"Invalid guess length. Please enter a {word_length}-letter word.") 
                elif not user_input.isalpha():
                    print("Invalid input. Please enter only alphabetic characters.") 
                else:
                    return user_input
            except EOFError:
                print("\nInput stream closed. Exiting game.") 
                sys.exit(1)

    def get_remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - self.__number_of_attempts

    def run(self) -> bool:
        while self.__number_of_attempts < self.MAX_ATTEMPTS:
            user_input = self._query_user_input()
            for index_char, char in enumerate(user_input):
                status = Status.NOT_FOUND # Default status
                # Check if the character is in the solution word at all
                if char in self.__solution.word:
                    # Get the positions of this character from the solution Word object
                    solution_positions = self.__solution.word[char]

                    # Convert int to list if it's a single position
                    if isinstance(solution_positions, int):
                        solution_positions = [solution_positions]

                    # Check for CORRECT_POSITION (1-based index in Word class)
                    if (index_char + 1) in solution_positions:
                        status = Status.CORRECT_POSITION
                    # Check for WRONG_POSITION (char is in word, but not at this specific index)
                    else:
                        status = Status.WRONG_POSITION
                else:
                    pass 

                self.__guess_history.update(self.__number_of_attempts, index_char, GuessEntry(char, status))

            self.__number_of_attempts += 1
            self.__guess_history.display()


            if user_input == str(self.__solution):
                print(f"Correct guess in {self.__number_of_attempts} attempts.") 
                
                return True
            else:
                if self.__number_of_attempts < self.MAX_ATTEMPTS:
                    print(f"Incorrect guess, Number of attempts left: {self.get_remaining_attempts()}") 
        print(f"No attempts left. The word was {str(self.__solution)}.") 
        print("Better luck next time!")
        return False