import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Takes player's guess
            guess = int(input("Take a guess: "))
            attempts += 1
            
            # For checking the correct number
            if guess < secret_number:
                print("Low! Try again.")
            elif guess > secret_number:
                print("High! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()