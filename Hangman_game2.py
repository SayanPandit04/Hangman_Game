import tkinter as tk
import random
from tkinter import messagebox

# Predefined list of words and hints
words_with_hints = [
    # Programming
    ('python', 'A popular programming language'),
    ('javascript', 'A scripting language mainly for web development'),
    ('java', 'A versatile programming language, also used for Android development'),
    ('hangman', 'The name of this game'),
    ('coding', 'What we are doing right now!'),
    ('software', 'Applications and programs are part of this'),
    ('engineer', 'A person who designs, builds, or maintains systems'),

    # Cricket
    ('viratkohli', 'King of cricket'),
    ('msdhoni', 'Captain cool'),
    ('rohitsharma', 'Hitman'),

    # Cars
    ('bmw', 'A German car brand known for Driving'),
    ('ferrari', 'A luxury sports car brand from Italy'),
    ('mercedes', 'A German car brand known for luxury'),

    # Food
    ('pizza', 'A popular Italian dish with cheese and toppings'),
    ('sushi', 'A Japanese dish featuring vinegared rice and seafood'),
    ('burger', 'A sandwich consisting of a cooked patty inside a bun'),

    # Travel
    ('paris', 'The capital of France, known for the Eiffel Tower'),
    ('london', 'The capital of the UK, known for the Big Ben'),
    ('tokyo', 'The capital of Japan'),

    # Technology
    ('laptop', 'A portable computer'),
    ('internet', 'A global system of interconnected computer networks'),
    ('software', 'Programs and applications on computers')
]

# Function to choose a random word and its hint from the list
def choose_word_and_hint():
    return random.choice(words_with_hints)

# Hangman game class
class HangmanGame:
    def __init__(self, root):  # Corrected __init__ method
        self.root = root
        self.root.title("Hangman Game with Hints")
        self.root.geometry('600x500')
        self.root.config(bg='#f0f8ff')

        self.word, self.hint = choose_word_and_hint()
        self.guessed_letters = []
        self.attempts_left = 6
        self.guessed_word = False

        self.display_word = tk.StringVar()
        self.update_display_word()

        self.message = tk.StringVar()
        self.message.set(f"You have {self.attempts_left} attempts left.")
        self.hint_message = tk.StringVar()
        self.hint_message.set(f"Hint: {self.hint}")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Game title
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Arial", 24, "bold"), bg='#f0f8ff', fg="#0f3057")
        self.title_label.pack(pady=10)

        # Display the hint
        self.hint_label = tk.Label(self.root, textvariable=self.hint_message, font=("Arial", 14), bg='#f0f8ff', fg="#00796b")
        self.hint_label.pack(pady=10)

        # Display the hangman word
        self.word_label = tk.Label(self.root, textvariable=self.display_word, font=("Arial", 30, "bold"), bg='#f0f8ff', fg="#00587a")
        self.word_label.pack(pady=20)

        # Input for guessing letters
        self.letter_entry = tk.Entry(self.root, font=("Arial", 18), width=5, justify='center', bg='#e7f2f8')
        self.letter_entry.pack(pady=10)

        # Button to submit the guess
        self.submit_button = tk.Button(self.root, text="Guess", font=("Arial", 14), command=self.guess_letter, bg="#009688", fg="white", activebackground="#00796b")
        self.submit_button.pack(pady=10)

        # Message label to show feedback
        self.message_label = tk.Label(self.root, textvariable=self.message, font=("Arial", 14), bg='#f0f8ff', fg="#f44336")
        self.message_label.pack(pady=20)

        # Reset button to start a new game
        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 14), command=self.reset_game, bg="#ff9800", fg="white", activebackground="#f57c00")
        self.reset_button.pack(pady=10)

        # Create hangman figure display
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='#f0f8ff', highlightthickness=0)
        self.canvas.pack(pady=10)
        self.draw_hangman()

    def draw_hangman(self):
        # Clear canvas before drawing
        self.canvas.delete("all")

        # Base stand (always visible)
        self.canvas.create_line(50, 180, 150, 180, width=4)
        self.canvas.create_line(100, 180, 100, 50, width=4)
        self.canvas.create_line(100, 50, 160, 50, width=4)
        self.canvas.create_line(160, 50, 160, 70, width=4)

        # Hangman parts (visible as attempts decrease)
        if self.attempts_left < 6:
            self.canvas.create_oval(140, 70, 180, 110, width=4)  # Head
        if self.attempts_left < 5:
            self.canvas.create_line(160, 110, 160, 150, width=4)  # Body
        if self.attempts_left < 4:
            self.canvas.create_line(160, 120, 140, 140, width=4)  # Left Arm
        if self.attempts_left < 3:
            self.canvas.create_line(160, 120, 180, 140, width=4)  # Right Arm
        if self.attempts_left < 2:
            self.canvas.create_line(160, 150, 140, 170, width=4)  # Left Leg
        if self.attempts_left < 1:
            self.canvas.create_line(160, 150, 180, 170, width=4)  # Right Leg

    def update_display_word(self):
        # Update the display with guessed letters or underscores, with spaces between each character
        display = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.display_word.set(display)

    def guess_letter(self):
        # Get the guessed letter
        guess = self.letter_entry.get().lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.message.set("You've already guessed that letter.")
            elif guess in self.word:
                self.guessed_letters.append(guess)
                self.message.set("Good guess!")
            else:
                self.attempts_left -= 1
                self.guessed_letters.append(guess)
                self.message.set(f"Wrong guess! {self.attempts_left} attempts remaining.")

            self.update_display_word()
            self.draw_hangman()
            self.check_game_over()

        else:
            self.message.set("Invalid input. Please guess a single letter.")

        self.letter_entry.delete(0, tk.END)  # Clear input field

    def check_game_over(self):
        # Check if the word is fully guessed or attempts are over
        if '_' not in self.display_word.get().replace(' ', ''):  # Removing spaces to check actual characters
            self.guessed_word = True
            self.message.set("Congratulations! You've guessed the word!")
            self.submit_button.config(state=tk.DISABLED)
            messagebox.showinfo("Hangman", "You won! The word was: " + self.word)
        elif self.attempts_left == 0:
            self.message.set(f"Game over! The word was: {self.word}")
            self.submit_button.config(state=tk.DISABLED)
            messagebox.showinfo("Hangman", "Game Over! The word was: " + self.word)

    def reset_game(self):
        # Reset the game state
        self.word, self.hint = choose_word_and_hint()
        self.guessed_letters = []
        self.attempts_left = 6
        self.guessed_word = False
        self.update_display_word()
        self.hint_message.set(f"Hint: {self.hint}")
        self.message.set(f"You have {self.attempts_left} attempts left.")
        self.submit_button.config(state=tk.NORMAL)
        self.draw_hangman()

# Create the main window
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()