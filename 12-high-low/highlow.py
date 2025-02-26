import art
import random

print(art.logo)  # Created on https://patorjk.com/software/taag/#p=display&f=Standard&t=High%20Low

print("Welcome to the High Low Number game\nThe number is between 1 and a number you choose\n")
high_limit = int(input("What number would you like to use for the high limit? "))
guess_limit = int(input("What is the maximum number of guesses? "))
target = random.randint(1, high_limit)
for tries in range(guess_limit):
    guess = int(input(f"Enter a guess between 1 and {high_limit}: "))
    if guess > target:
        print(f"Your guess of {guess} was too high. {guess_limit - tries - 1} guesses remaining")
    elif guess < target:
        print(f"Your guess of {guess} was too low. {guess_limit - tries - 1} guesses remaining")
    else:
        print(f"Your guess of {guess} was correct after {tries + 1} attempts. ")
        break
if tries >= guess_limit:
    print(f"Too many guesses you lose the number was {target}\nTry again") 
print("Thank you for playing the High Low Number game")