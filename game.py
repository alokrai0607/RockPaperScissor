import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice in {'rock', 'paper', 'scissors', 'q'}:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'q' to quit.")

def determine_winner(user_choice, computer_choice):
    if user_choice == 'q':
        return 'quit', None

    if user_choice == computer_choice:
        return 'draw', None
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win', user_choice
    else:
        return 'lose', computer_choice

def display_result(result, choice):
    if result == 'win':
        print(f"You win! Computer chose {choice}.")
    elif result == 'lose':
        print(f"You lose! Computer chose {choice}.")
    else:
        print("It's a draw!")

def play_game():
    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            break

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result, choice = determine_winner(user_choice, computer_choice)
        display_result(result, choice)

        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        else:
            draws += 1

    print("Final Score:")
    print(f"You: {user_score} wins, Computer: {computer_score} wins, Draws: {draws}")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors game!")
    play_game()
