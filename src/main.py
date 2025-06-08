from name import Name
from player import Player
from score import Score
from word import Word
from word_list_from_json_file import WordListFromJsonFile
from guess_entry import GuessEntry
from guess_history import GuessHistory
from guess import Guess
from game import Game
from scoreboard import Scoreboard 
from game_ui import GameUI

def main():
    game_ui = GameUI()
    game_ui.run()

if __name__ == "__main__":
    main()