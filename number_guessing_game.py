import random

secret_number = random.randint(1, 100)
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts.")
        break
else:
    print(f"Game Over! You have used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}.")