import random
choices = ["rock", "paper", "scissors"]
winning_moves = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

is_game_rigged = False
SECRET_CODE = "RIGMYGAME"
def get_player_choice():
    while True:
        player_input = input("Choose (rock, paper, scissors) or enter secret code: ").lower()
        if player_input in choices:
            return player_input
        elif player_input == SECRET_CODE.lower():
            activate_rigging()
            continue
        else:
            print("Invalid choice. Please choose 'rock', 'paper', 'scissors', or the secret code.")

def get_computer_choice(player_choice):

    if is_game_rigged:
        print("Computer: 'My AI is feeling particularly strong today!'")
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

def activate_rigging():
    global is_game_rigged
    is_game_rigged = True
    print("\n--- RIGGING ACTIVATED! The computer will now try to win every round. ---")
def main_game_loop():
    print("Welcome to Rock-Paper-Scissors!")
    print(f"Enter the secret code '{SECRET_CODE}' to rig the game for the computer.")
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

