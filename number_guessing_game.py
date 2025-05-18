import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("\n\n_____________Welcome to the Number Guessing Game!___________\n")
    print("_________I'm thinking of a number between 1 and 100.________\n")
    
    while True:
        try:
            # Takes player's guess
            print("\n")
            guess = int(input("\t\tTake a guess: "))
            attempts += 1
            
            # For checking the correct number
            if guess < secret_number:
                print("\t\tLow! Try again.")
            elif guess > secret_number:
                print("\t\tHigh! Try again.")
            else:
                print(f"\t\tCongratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("\t\tPlease enter a valid number.")

number_guessing_game()