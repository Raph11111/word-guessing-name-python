import json
import os
from score import Score
class Scoreboard:
    
    __SCOREBOARD_FILE = "scoreboard.json"
    __MAX_ENTRIES = 10

    def __init__(self, file_path: str = __SCOREBOARD_FILE) -> None:
        self.__file_path = file_path
        self.__scores: list[tuple[str, int]] = []
        self.load_scores()

    def __load_scores(self) -> None:
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.__scores = [(entry[0], entry[1]) for entry in data if isinstance(entry, list) and len(entry) == 2 and isinstance(entry[0], str) and isinstance(entry[1], int)]
                self.__scores.sort(key=lambda x: x[1], reverse=True)
                self.__scores = self.__scores[:self.__MAX_ENTRIES]
            except (json.JSONDecodeError, FileNotFoundError, TypeError) as e:
                print(f"Error loading scoreboard: {e}. Starting with an empty scoreboard.")
                self.__scores = []
        else:
            print("Scoreboard file not found. A new one will be created.")
            self.__scores = []

    def __save_scores(self) -> None:
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(self.__scores, file, indent=4)
        except IOError as e:
            print(f"Error saving scoreboard: {e}")

    def add_score(self, player_name: str, score: int) -> None:
        self.__scores.append((player_name, score))
        self.__scores.sort(key=lambda x: x[1], reverse=True)
        self.__scores = self.__scores[:self.__MAX_ENTRIES]
        self.__save_scores()

    def display(self) -> None:
        print("\n--- Scoreboard ---")
        if not self.__scores:
            print("No scores yet. Be the first to play!")
        else:
            print(f"{'Rank':<5} {'Player':<15} {'Score':<10}")
            print("-" * 30)
            for i, (name, score) in enumerate(self.__scores):
                print(f"{i+1:<5} {name:<15} {score:<10}")
        print("------------------\n")

    
    def load_scores(self) -> None:
        self.__load_scores()

    def save_scores(self) -> None:
        self.__save_scores()