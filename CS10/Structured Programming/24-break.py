from random import randint
guess_number = 0
pin = randint(0,999)
print("Thank you for using the ATM!")
while(guess_number < 5):
    print("Enter your three digit PIN:")
    guess=int(input())
    if(guess == pin):
        print("CORRECT! Your PIN was entered correctly!")
        break
    else:
        guess_number+=1
        print("ERROR! You have used "+str(guess_number)+" guesses!")

if(guess != pin):
    print("Too many guesses. Shutting down.")

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

#What is the function of this code?
    #This code's function is the BREAK command. BREAK can be used to exit a loop. This is usually after it fufills a certain condition. 
    #In this case, it exits the loop of guessing the random pin after too many guesses. 
    #Additionally, it helps you use the RANDINT command, which allows you to generate a random number from a specific range.
#Why does the code start with the line “from random import randint”? Is this necessary for the code to run?
    #This code is necessary to run this program. It imports the set of commands shown above (RANDINT)
    #Python does not automatically do this, so without importing first, the program will not recognize RANDINT as a command and will not run.
#What does the guessNumber += 1 command do?
    #The "+= 1" command adds a certain integer (in this case, 1) to a variable without knowing the varible.
    #This is useful, as it allows you to add without knowing what the variable is, as it may depend on user input.
    #For example, this is needeed to know how many guesses have been used. This number will be dependant on the user input, so it is crucial for the code to have this command.
    #It is the same as "variable = variable + 1", just more efficent
#What does the “break” command do to the code?
    #The BREAK command is used to exit a loop. This is used to exit a loop without making the condition that makes the loop run turn FLASE
    #This is shown in how the BREAK breaks the user out of the loop when the get the PIN correct, even if the guess_number was still less than 5
    #It broke the code out of the loop without fufilling the WHILE condition (turn it FALSE)
