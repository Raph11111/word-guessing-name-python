from guess import Guess
from word_list_from_json_file import WordListFromJsonFile
from player import Player
from scoreboard import Scoreboard 
class Game:
    def __init__(self)->None:
        self.__player = Player()
        print(f"Welcome, {self.__player.name}!")
        self.__word_list = WordListFromJsonFile("assets/sample_wordles.json")
        self.__guess = None
        self.__scoreboard = Scoreboard() # Initialize the scoreboard

    def run(self)->None:
        print("Let's start the game!")
        index = 0
        while (index < self.__word_list.get_number_of_words()):
            solution = self.__word_list.get_word(index)
            self.__guess = Guess(solution)
            result = self.__guess.run() # result is True if won, False if lost
            self.__player.score.add((self.__guess.get_remaining_attempts() + 1) * 10)

            if result:
                print("You won!")
                print(f"Your current score is: {self.__player.score.points}")
            else:
                print(f"Your current score is: {self.__player.score.points}")


            user_input2 = input("Do you want to play again?(y/n) ").upper()
            if user_input2 == "Y":
                index = 0
            elif user_input2 == "N":
                print(f"Your final score is: {self.__player.score.points}")
                # am ENde des SPiels machen wir alle updates 
                player_score = self.__player.score.points
                player_name = str(self.__player.name) # Get the player's name as a string
                self.__scoreboard.add_score(player_name, player_score)
                print(f"player_score: {player_score}, player_name: {player_name}")
                self.__scoreboard.display() # Display the scoreboard after each round
                self.__scoreboard.save_scores()

                exit()
            else:
                print("Invalid input. Exiting game.")
                self.__scoreboard.save_scores()
                exit()
            index += 1
        print("No more words to play. Game over!")
        self.__scoreboard.save_scores() # Save scores at the end of all words
