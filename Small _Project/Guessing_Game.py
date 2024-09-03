from random import randint

def guessing_game():
    while True:
        guessNumber = int(input("Enter your guess between 1 to 9: "))
        randomNumber = randint(1, 9)

        if guessNumber == randomNumber:
            print("You have won")
        else:
            print("You have lost")
            print("Random Number was:", randomNumber)

        # Ask the user if they want to continue
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
guessing_game()
