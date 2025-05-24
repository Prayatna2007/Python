import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_left=10
    
    print("\n\n_____________Welcome to the Number Guessing Game!___________\n")
    print("_________I'm thinking of a number between 1 and 100.________\n")
    
    while (1):
        try:
            # Takes player's guess
            print("\n")
            print(f"You have total {attempts_left} attempts left")
            guess = int(input("\t\tTake a guess: "))
            attempts += 1
            attempts_left=attempts_left-1
            
            # For checking the correct number
            if attempts_left==0:
                print("You lost .....")
                exit(1)
            elif guess < secret_number:
                print("\t\tLow! Try again.")
            elif guess > secret_number:
                print("\t\tHigh! Try again.")
            else:
                print(f"\t\tCongratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("\t\tPlease enter a valid number.")

number_guessing_game()