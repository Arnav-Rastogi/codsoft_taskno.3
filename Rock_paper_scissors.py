import tkinter as tk
import random

# Game logic
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    winner = determine_winner(user_choice, computer_choice)

    # Update labels
    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    comp_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    if winner == "tie":
        result_label.config(text="It's a tie!")
    elif winner == "user":
        result_label.config(text="You win! 🎉")
        user_score += 1
    else:
        result_label.config(text="You lose! 😞")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Result Display
user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, fg="red")
reset_btn.pack(pady=10)

# Run the GUI
root.mainloop()
