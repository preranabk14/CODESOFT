import random

def computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def check_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please select rock, paper, or scissors.")
            continue

        computer_pick = computer_choice()
        print(f"The computer chose: {computer_pick}")

        result = check_winner(user_input, computer_pick)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

        replay = input("Do you want to play another round? (yes/no): ").lower()
        if replay != "yes":
            break

    print("Game over! Thanks for playing.")

rock_paper_scissors()
