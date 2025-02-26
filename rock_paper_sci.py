import random
#random module is used to generate random numbers
#random.choice() is used to choose a random element from a list

#function for computer choice

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)
#or we can write- return random.choice(['r', 'p', 's'])

#function for user choice
def get_user_choice():
    user_choice = input("enter rock(r), paper(p), or scissors(s): ").lower()
    while user_choice not in ['r', 'p', 's']:
        print("choice is invalid...please try again")
        user_choice = input("enter rock(r), paper(p), or scissors(s): ").lower()
    return user_choice
#or we can write- return input("enter rock(r), paper(p), or scissors(s): ").lower()
# lower() is used to convert the input to lowercase
# \ is used to break the line
#function to determine winner
def determine_winner(user_choice, computer_choice):
    choices1 = {"r": "rock", "p": "paper", "s": "scissors"}    # dictionary to convert user choice to string
    print(f"you chose {choices1[user_choice]}")
    print(f"computer chose {choices1[computer_choice]}")

    if user_choice == computer_choice:
        return "it is a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
        return "you win!"
    else:
        return "you lose, computer wins!"
    
#function to play the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(determine_winner(user_choice, computer_choice))

#function to ask user if they want to play again
def play_again():
    play_again = input("do you want to play again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        print("invalid input, please try again")
        play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
        play_again()
    else:
        print("thanks for playing!")
#main function
def main():
    play_game()
    play_again()

if __name__ == "__main__":
    main()

#this is a simple rock, paper, scissors game
#the computer chooses a random choice and the user chooses a choice
#the winner is determined based on the choices
#the user can play again if they want
#the user can choose to play again or not
#the game is played until the user chooses to not play again
#the game is played in the terminal
#the game is written in python

