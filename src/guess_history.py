from guess_entry import GuessEntry, Status 

class GuessHistory:
    GREEN_COLOR = "\033[32m"  # ANSI-Escape-Code für grünen Text
    BLUE_COLOR = "\033[34m"   # ANSI-Escape-Code für blauen Text
    RESET_COLOR = "\033[0m"   # ANSI-Escape-Code zum Zurücksetzen der Textfarbe

    def __init__(self, max_attempts: int, word_length: int) -> None:
        self.__max_attempts = max_attempts
        self.__word_length = word_length
        # Initialisiert die 2D-Historienstruktur mit Platzhalter-GuessEntry-Objekten.
        # Jeder Platzhalter repräsentiert ein noch nicht geratenes Zeichen.
        self.__history: list[list[GuessEntry]] = [
            [GuessEntry("_", Status.NOT_FOUND) for _ in range(word_length)]
            for _ in range(max_attempts)
        ]

    def __getitem__(self, idx: int) -> list[GuessEntry]:
        if not (0 <= idx < self.__max_attempts):
            raise IndexError(f"Der Versuchsindex {idx} ist außerhalb der Grenzen. Er muss zwischen 0 und {self.__max_attempts - 1} liegen.")
        return self.__history[idx]

    @property
    def history(self) -> list[list[GuessEntry]]:
        return self.__history

    def update(self, attempt: int, index: int, entry: GuessEntry) -> None:
        if not isinstance(entry, GuessEntry):
            raise TypeError("Der Eintrag muss eine Instanz von GuessEntry sein.")
        if not (0 <= attempt < self.__max_attempts):
            raise IndexError(f"Die Versuchsnummer {attempt} ist außerhalb der Grenzen. Sie muss zwischen 0 und {self.__max_attempts - 1} liegen.")
        if not (0 <= index < self.__word_length):
            raise IndexError(f"Der Zeichenindex {index} ist außerhalb der Grenzen. Er muss zwischen 0 und {self.__word_length - 1} liegen.")
            
        self.__history[attempt][index] = entry

    def get_attempt(self, attempt: int) -> list[GuessEntry]:
        return self.__getitem__(attempt)

    @property
    def history(self) -> list[list[GuessEntry]]:
        return self.__history

    def display(self) -> None:
        print("\n______Rate Historie______")
        for i, attempt_entries in enumerate(self.__history):
            for entry in attempt_entries:
                char_to_print = entry.char.upper()
                if entry.status == Status.CORRECT_POSITION:
                    print(f"{self.GREEN_COLOR}{char_to_print}{self.RESET_COLOR}", end=" ")
                elif entry.status == Status.WRONG_POSITION:
                    print(f"{self.BLUE_COLOR}{char_to_print}{self.RESET_COLOR}", end=" ")
                else:
                    # Für NOT_FOUND oder anfängliche leere Felder, in Standardfarbe drucken
                    print(f"{char_to_print}{self.RESET_COLOR}", end=" ")
            print() # Neue Zeile nach jedem Versuch
        print("_________________________\n")