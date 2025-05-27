import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_left = 10
    print("\n\n This is a Number Guessing game where you hvae to guess a number under 10 attempts and if you failed to find the correct number under the given attempts you lose.....\n\n")
    print("\n\n_____________Welcome to the Number Guessing Game!___________\n")
    print("_________I'm thinking of a number between 1 and 100.________\n")
    
    while True:
        try:
            print(f"\nYou have {attempts_left} attempts left")
            guess = int(input("\t\tTake a guess: "))
            attempts += 1
            attempts_left -= 1
            
            if attempts_left == 0 and guess != secret_number:
                print("\t\tYou lost...")
                print("\t\tThe secret number was", secret_number)
                break
            elif guess == secret_number:
                print(f"\t\tCongratulations! You guessed the number in {attempts} attempts!")
                break
            elif guess < secret_number - 20:
                print("\t\tVery Low! Try again.")
            elif guess < secret_number:
                print("\t\tLow! Try again.")
            elif guess > secret_number + 20:
                print("\t\tVery High! Try again.")
            elif guess > secret_number:
                print("\t\tHigh! Try again.")
        except ValueError:
            print("\t\tPlease enter a valid number.")

number_guessing_game()