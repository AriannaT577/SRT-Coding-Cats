from random import randint
attempts = 0
guess = ""
answer =""
print("Welcome to the guessing game! You have to try to guess the correct number. Are you ready to start? (Y/N)")
ready = input()

while ready == "Y":
    print("What numbers do you want the secret number to fall between? Please type in the lowest possible number:")
    low = int(input())
    print("Great! Please type in the highest possible number:")
    high = int(input())
    answer = randint(low,high)
    print("Please guess a number from "+str(low)+" and "+str(high)+" inclusive.")

    while answer != guess:
        guess = int(input())
        if answer == guess:
            print("Correct! Your a guessing whizz. You guessed the number "+str(answer)+"!")
            print("Do you want to play again? (Y/N)")
            again = input()
            if again == "Y":
                print("Nice!")
                break
            elif again == "N":
                print("Hope you had fun!")
                ready == "N"
                break
            
        else:
            attempts+=1

            if answer <= guess:
                print("Too high!")
            elif answer >= guess:
                print("Too low!")
            
            print("You have used "+str(attempts)+" guesses. Try again!")
            
            if attempts <=3:
                print("You'll get it eventually, keep at it!")
            elif attempts== 4:
                print("Yikes, this is taking you a while.")
            elif attempts== 5:
                print("Oh my, are you sure you know how numbers work?")
            elif attempts == 6:
                print("Whoever told you to be yourself clearly lied to you.")
            elif attempts == 7:
                print("I didn't know a first-grader was playing this game.")
            elif attempts == 8:
                print("I envy the people who have never met you.")
            elif attempts == 9:
                print("Your train of thought is clearly going nowhere.")
            elif attempts == 10:
                print("Were you dropped as a baby?")
            elif attempts == 11:
                print("You should apologize to the tree thats producing the oxygen your wasting.")
            elif attempts == 12:
                print("Are you naturally like this, or do you put in effort?")
            else:
                print("You are taking so long this code ran out of insults. Not everyone can do that.")
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

if ready != "Y":
    print("Come back when you are!")
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
