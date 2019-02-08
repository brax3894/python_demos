import random


random_number = random.randint(1,10)
player_input = None

while True:
    player_input = input("Guess my secret number (1-10) : ")
    if int(player_input) != random_number:
        while int(player_input) != random_number:
            if int(player_input) > random_number:
                print("you guessed too high, guess again")
            elif int(player_input) < random_number:
                print("you guessed too low, guess again")
            player_input = input("guess again: ")
        else:
            print("Nice guess! you win")
            break




play_again = input("Would you like to play again? (y/n)")
if play_again == "y":
    random_number = random.randint(1, 10)
    player_input = None


else:
    game_on=False
    print("Thank you for playing")








