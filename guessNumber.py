import random
#system generated random number
number = random.randint(1,5)
attempts = 0
print("Welcome to the Guessing Game")
while True:
    guess = int(input("Enter your guess (between 1 and 5): "))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        print(f"It took you {attempts} attempts.")
        break