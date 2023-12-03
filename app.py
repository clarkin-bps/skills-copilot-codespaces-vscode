import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Enter your choice (rock/paper/scissors): ")
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose {user_choice}, computer chose {computer_choice}. {result}")

play_game()