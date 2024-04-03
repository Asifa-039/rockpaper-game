import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "Computer wins!"
    return (computer_choice, result)

# Function to play the game
def play_game(user_choice):
    computer_choice, result = determine_winner(user_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Define choices
choices = ["rock", "paper", "scissors"]

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Create label for result display
result_label = tk.Label(window, text="", font=('Arial', 12))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Run the application
window.mainloop()
