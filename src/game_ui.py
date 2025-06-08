import customtkinter as ctk
from tkinter import messagebox
from player import Player
from word_list_from_json_file import WordListFromJsonFile
from guess import Guess
from scoreboard import Scoreboard
from word import Word
from guess_entry import GuessEntry, Status
import os

class GameUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Word Guessing Game")
        self.root.geometry("800x600")
        
        # Player ohne Konsoleneingabe initialisieren
        self.player = Player("GUI_Player")  # Temporärer Name
        self.show_welcome_screen()
        self.player.name._Name__name = ""  # Zurücksetzen für GUI-Eingabe
        
        self.word_list = None
        self.current_guess = None
        self.scoreboard = Scoreboard()
        self.current_word_index = 0
        
        # Styling
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.show_welcome_screen()
        
    def show_welcome_screen(self):
        self.clear_window()
        
        welcome_frame = ctk.CTkFrame(self.root)
        welcome_frame.pack(pady=100, padx=100, fill="both", expand=True)
        
        ctk.CTkLabel(welcome_frame, text="Welcome to Word Guessing Game!", 
                    font=("Arial", 20)).pack(pady=20)
        
        if not str(self.player.name):
            name_button = ctk.CTkButton(welcome_frame, text="Enter Your Name", 
                                      command=self.show_name_input)
            name_button.pack(pady=10)
        else:
            ctk.CTkLabel(welcome_frame, text=f"Welcome back, {self.player.name}!",
                        font=("Arial", 14)).pack(pady=10)
        
        play_button = ctk.CTkButton(welcome_frame, text="Play Game", 
                                   command=self.start_game, 
                                   state="normal" if str(self.player.name) else "disabled")
        play_button.pack(pady=10)
        
        scoreboard_button = ctk.CTkButton(welcome_frame, text="View Scoreboard", 
                                        command=self.show_scoreboard)
        scoreboard_button.pack(pady=10)
        
        exit_button = ctk.CTkButton(welcome_frame, text="Exit", 
                                   command=self.root.quit)
        exit_button.pack(pady=10)
        
        self.play_button = play_button
    
    def show_name_input(self):
        self.clear_window()
        
        name_frame = ctk.CTkFrame(self.root)
        name_frame.pack(pady=100, padx=100, fill="both", expand=True)
        
        ctk.CTkLabel(name_frame, text="Enter your name (min 4 alphanumeric chars):", 
                    font=("Arial", 14)).pack(pady=20)
        
        self.name_entry = ctk.CTkEntry(name_frame)
        self.name_entry.pack(pady=10)
        
        submit_button = ctk.CTkButton(name_frame, text="Submit", 
                                     command=self.process_name_input)
        submit_button.pack(pady=10)
        
        back_button = ctk.CTkButton(name_frame, text="Back to Menu", 
                                   command=self.show_welcome_screen)
        back_button.pack(pady=10)
    
    def process_name_input(self):
        name = self.name_entry.get().strip()
        try:
            if len(name) < 4 or not name.isalnum():
                raise ValueError("Name must be at least 4 alphanumeric characters")
            
            # Direkte Zuweisung des Namens
            self.player.name._Name__name = name
            
            # Word List initialisieren
            if not os.path.exists("assets"):
                os.makedirs("assets")
            if not os.path.exists("assets/sample_wordles.json"):
                with open("assets/sample_wordles.json", "w") as f:
                    f.write('[{"word": "APPLE"}, {"word": "BRAIN"}, {"word": "CLOUD"}, {"word": "DANCE"}, {"word": "EARTH"}]')
            
            self.word_list = WordListFromJsonFile("assets/sample_wordles.json")
            messagebox.showinfo("Success", f"Welcome, {self.player.name}!")
            self.show_welcome_screen()
            
        except ValueError as e:
            messagebox.showerror("Invalid Name", str(e))
            self.name_entry.focus()
    
    def start_game(self):
        if not str(self.player.name):
            messagebox.showerror("Error", "Please enter your name first")
            return
            
        if self.current_word_index >= self.word_list.get_number_of_words():
            messagebox.showinfo("Game Over", "No more words to play!")
            self.show_welcome_screen()
            return
            
        self.clear_window()
        
        solution = self.word_list.get_word(self.current_word_index)
        self.current_guess = Guess(solution)
        
        # Game UI
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(pady=10)
        ctk.CTkLabel(title_frame, text=f"Word Guessing Game - Player: {self.player.name}", 
                     font=("Arial", 16)).pack()
        
        self.history_frame = ctk.CTkFrame(self.root)
        self.history_frame.pack(pady=20)
        self.update_history_display()
        
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=20)
        
        ctk.CTkLabel(input_frame, text="Enter your guess:").pack(side="left", padx=10)
        self.guess_entry = ctk.CTkEntry(input_frame, width=200)
        self.guess_entry.pack(side="left", padx=10)
        self.guess_entry.bind("<Return>", lambda e: self.process_guess())
        
        submit_button = ctk.CTkButton(input_frame, text="Submit", 
                                    command=self.process_guess)
        submit_button.pack(side="left", padx=10)
        
        menu_button = ctk.CTkButton(self.root, text="Back to Menu", 
                                   command=self.return_to_menu)
        menu_button.pack(pady=10)
    
    def update_history_display(self):
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        if not self.current_guess:
            return
            
        for attempt in range(Guess.MAX_ATTEMPTS):
            attempt_frame = ctk.CTkFrame(self.history_frame)
            attempt_frame.pack(pady=5)
            
            for char_pos in range(Word.get_word_length()):
                if attempt < self.current_guess._Guess__number_of_attempts:
                    entry = self.current_guess._Guess__guess_history.history[attempt][char_pos]
                else:
                    entry = GuessEntry("_", Status.NOT_FOUND)
                
                char_label = ctk.CTkLabel(attempt_frame, text=entry.char, width=40, height=40,
                                         font=("Arial", 16), corner_radius=5)
                
                if entry.status == Status.CORRECT_POSITION:
                    char_label.configure(fg_color="green")
                elif entry.status == Status.WRONG_POSITION:
                    char_label.configure(fg_color="gold")
                else:
                    char_label.configure(fg_color="gray")
                
                char_label.pack(side="left", padx=2)
    
    def process_guess(self):
        guess = self.guess_entry.get().strip().upper()
        self.guess_entry.delete(0, 'end')
        
        if len(guess) != Word.get_word_length():
            messagebox.showerror("Error", f"Guess must be {Word.get_word_length()} letters long")
            return
            
        if not guess.isalpha():
            messagebox.showerror("Error", "Guess must contain only letters")
            return
            
        # Process guess
        for index_char, char in enumerate(guess):
            status = Status.NOT_FOUND
            if char in self.current_guess._Guess__solution.word:
                solution_positions = self.current_guess._Guess__solution.word[char]
                if isinstance(solution_positions, int):
                    solution_positions = [solution_positions]
                if (index_char + 1) in solution_positions:
                    status = Status.CORRECT_POSITION
                else:
                    status = Status.WRONG_POSITION
            
            self.current_guess._Guess__guess_history.update(
                self.current_guess._Guess__number_of_attempts,
                index_char,
                GuessEntry(char, status)
            )
        
        self.current_guess._Guess__number_of_attempts += 1
        self.update_history_display()
        
        solution_word = str(self.current_guess._Guess__solution)
        
        if guess == solution_word:
            points = (self.current_guess.get_remaining_attempts() + 1) * 10
            self.player.score.add(points)
            messagebox.showinfo("Congratulations!", 
                              f"You guessed correctly in {self.current_guess._Guess__number_of_attempts} attempts!\n"
                              f"You earned {points} points.\n"
                              f"Your total score: {self.player.score.points}")
            self.current_word_index += 1
            self.ask_to_play_again()
        elif self.current_guess._Guess__number_of_attempts >= Guess.MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", 
                              f"No attempts left. The word was {solution_word}.\n"
                              f"Your total score: {self.player.score.points}")
            self.current_word_index += 1
            self.ask_to_play_again()
    
    def ask_to_play_again(self):
        response = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if response:
            self.start_game()
        else:
            self.scoreboard.add_score(str(self.player.name), self.player.score.points)
            self.scoreboard.save_scores()
            self.show_welcome_screen()
    
    def show_scoreboard(self):
        self.clear_window()
        
        scoreboard_frame = ctk.CTkFrame(self.root)
        scoreboard_frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        ctk.CTkLabel(scoreboard_frame, text="Scoreboard", 
                    font=("Arial", 20)).pack(pady=20)
        
        self.scoreboard.load_scores()
        scores = self.scoreboard._Scoreboard__scores
        
        if not scores:
            ctk.CTkLabel(scoreboard_frame, text="No scores yet. Be the first to play!").pack()
        else:
            headers_frame = ctk.CTkFrame(scoreboard_frame)
            headers_frame.pack(fill="x")
            ctk.CTkLabel(headers_frame, text="Rank", width=50).pack(side="left")
            ctk.CTkLabel(headers_frame, text="Player", width=200).pack(side="left")
            ctk.CTkLabel(headers_frame, text="Score", width=100).pack(side="left")
            
            for i, (name, score) in enumerate(scores):
                score_frame = ctk.CTkFrame(scoreboard_frame)
                score_frame.pack(fill="x")
                ctk.CTkLabel(score_frame, text=str(i+1), width=50).pack(side="left")
                ctk.CTkLabel(score_frame, text=name, width=200).pack(side="left")
                ctk.CTkLabel(score_frame, text=str(score), width=100).pack(side="left")
        
        back_button = ctk.CTkButton(scoreboard_frame, text="Back to Menu", 
                                   command=self.show_welcome_screen)
        back_button.pack(pady=20)
    
    def return_to_menu(self):
        response = messagebox.askyesno("Save Progress?", 
                                      "Do you want to save your progress before exiting?")
        if response:
            self.scoreboard.add_score(str(self.player.name), self.player.score.points)
            self.scoreboard.save_scores()
        
        self.show_welcome_screen()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()