import random
choices = ["rock", "paper", "scissors"]
winning_moves = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}
is_game_rigged = False

def get_player_choice():
    while True:
        player_input = input("Choose (rock, paper, scissors): ").lower()
        if player_input in choices:
            return player_input
        elif player_input == 'exit':
            return 'exit'
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice(player_choice):
    if is_game_rigged:
        return winning_moves[player_choice]
    else:
        return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    print("-" * 20)

def main_game_loop():
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'exit' to quit at any time.")

    while True:
        player_choice = get_player_choice()

        if player_choice == 'exit':
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice(player_choice)
        determine_winner(player_choice, computer_choice)

if __name__ == "__main__":
    main_game_loop()
