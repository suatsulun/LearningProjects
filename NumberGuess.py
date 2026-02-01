

import random

low = 1
high = 100

number = random.randint(low, high)
guesses = 0


is_playing = True

while is_playing:
    guess = input(f"Guess a number between {low} and {high}: ")
    if guess.isdigit() and low <= int(guess) <= high:
        guesses += 1
        guess = int(guess)
        if guess == number:
            is_playing = False
        elif number < guess < number +5 :
            print(f"{guess} is just a little high")
        elif number > guess > number - 5:
            print(f"{guess} is just a little low")
        elif number < guess:
            print(f"{guess} is too high")
        elif number > guess:
            print(f"{guess} is too low")
    else:
        print(f"You must guess a number between {low} and {high}")

print(f"Well done! You have found the number. It was {number}")
print(f"You guessed the number in {guesses} guessess.")