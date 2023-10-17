import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)
    attempts = 0

    while True:
        try:
            user_guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
            attempts += 1

            if user_guess < lower_limit or user_guess > upper_limit:
                print(f"Please enter a number between {lower_limit} and {upper_limit}.")
                continue

            if user_guess < number_to_guess:
                print("Too low! Try a higher number.")
            elif user_guess > number_to_guess:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
