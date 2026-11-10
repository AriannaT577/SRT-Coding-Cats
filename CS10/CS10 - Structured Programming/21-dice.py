from random import randint
print("Lets roll some dice! How many sides do you want your die to have?\nPlease pick between 2, 3, 4, or 6.")
sides = int(input())
logo = ("         /\\\\\
\n        // \\\\\
\n       //___\\\\\
\n      //-----\\\\             __________\
\n     //       \\\            ----||----\
\n    /          \\         ---    ||\
\n   /         ___\\_____---       ||\
\n  /                             ||\
\n /       o                      ||\
\n/             \'     o           || ")

print("The die are rolling!")
if sides == 2 or 3 or 4 or 6:
    die1= randint(1,sides)
    die2 = randint(1,sides)
    print("\nDie #1 = "+str(die1)+"\nDie #2 = "+str(die2)+"\n")
    print("You have rolled a "+str(die1+die2)+"!")
    print(logo)

else:
    print("Sorry! I am unable to roll a die with that many sides. Please restart program to try again.")

