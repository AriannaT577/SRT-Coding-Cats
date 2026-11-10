#import random 
#random.randint(1,10)#random int from 1-10
#random.random()#random float
#random.choice(seqence)#random number from sequence

from random import randint
answer = randint(1,10)#returns random int from 1-10
attempts = 0
print("Welcome to the guessing game! You have 3 tries to guess the correct number.")

if attempts == 0:
    print("Please guess a number from 1-10 inclusive")
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
        
    else:
        attempts+=1
        print("Sorry, not quite correct! Try again!")
        print("Please guess a number from 1-10 inclusive")
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
        
        else:
            attempts+=1
            print("Sorry, not quite correct! Try again!")
            print("Please guess a number from 1-10 inclusive")
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
        
            else:
                attempts+=1
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
