print("Are you curious what you can do legally? Lets test! \nMay I know your name?")
name = input()

print("Hello",name,"! Next, what is your age?")
age = int(input())

if age <= 15:
    print("Sorry, you can't drive",name,".")   

elif ((age>=18) and (age<=24)):
    print ("You can drive and vote but you can't rent a car",name,".")

elif (age>=25):
    print("You can do anything that's legal",name,".")

else:
    print("You can drive, but you can't vote",name,".")

#logo
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
