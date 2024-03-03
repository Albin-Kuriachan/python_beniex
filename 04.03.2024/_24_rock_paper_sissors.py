""".Implement the game rock, paper, scissors
                        Rock smashes scissors.
                        Paper covers rock.
                        Scissors cut paper."""

import random


def find_winner(player_choice, computer_choice):
    if computer_choice == player_choice:
        return "It's a tie!"

    elif (player_choice == "R" and computer_choice == "S") or \
            (player_choice == "S" and computer_choice == "P") or \
            (player_choice == "P" and computer_choice == "R"):
        return "Player Win!"
    else:
        return "Computer Win!"


def game():
    print("Welcome to Rock, Paper, Scissors!")
    choose = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors",
    }
    player_point = 0
    computer_point = 0
    while True:
        player_choice = input("Enter your choice (R, P, or S): ").upper()
        computer_choice = random.choice(list(choose.keys()))

        if player_choice not in choose:
            print("Invalid choice. Please try again.")
            continue

        p = choose[player_choice]
        c = choose[computer_choice]
        print(f'Player choice   :{p}')
        print(f'Computer choice :{c}')

        result = find_winner(player_choice, computer_choice)
        print(result)

        if result == "Player Win!":
            player_point += 1
        elif result == "Computer Win!":
            computer_point += 1

        print('Player Point      Computer Point')
        print("   ", player_point, "                 ", computer_point)

        play_again = input("Do you want to play again? (Any key to continue / No to exit): ").lower()
        if play_again == "no":
            if player_point > computer_point:
                print("Player is the Champion")
            elif player_point < computer_point:
                print("Computer is the champion")
            else:
                print("Game is Tie !")
            print("Thanks for playing!")
            break


result = game()
