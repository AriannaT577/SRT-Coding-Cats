from random import randint
attempts = 0
print("Welcome to the guessing game! You have 3 tries to guess the correct number.")
print("What numbers do you want the secret number to fall between? Please type in the lowest possible number:")
low = int(input())
print("Great! Please type in the highest possible number:")
high = int(input())
answer = randint(low,high)
print("Please guess a number from "+str(low)+" and "+str(high)+" inclusive.")


while attempts <= 2:
    guess = int(input())
    if answer == guess:
        print("Correct! Your a guessing whizz. You guessed the number "+str(answer)+"!")
        print("         /\\\\\
\n        // \\\\\
\n       //___\\\\\
\n      //-----\\\\             __________\
\n     //       \\\            ----||----\
\n    /          \\         ---    ||\
\n   /         ___\\_____---       ||\
\n  /                             ||\
\n /       o                      ||\
\n/             \'     o           || ")
        break
    else:
        attempts+=1
        print("Sorry, not quite correct! Try again!")

if attempts == 3:
    print("Your out of attempts. The answer was "+str(answer)+"!")
    print("         /\\\\\
\n        // \\\\\
\n       //___\\\\\
\n      //-----\\\\             __________\
\n     //       \\\            ----||----\
\n    /          \\         ---    ||\
\n   /         ___\\_____---       ||\
\n  /                             ||\
\n /       o                      ||\
\n/             \'     o           || ")
