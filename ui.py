from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/app', methods=['GET', 'POST'])
def game():
    user_choice = None
    computer_choice = None
    result = None

    if request.method == 'POST':
        user_choice = request.form.get('choice')
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = determine_winner(user_choice, computer_choice)

    return render_template('app.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

if __name__ == '__main__':
    app.run(debug=True)