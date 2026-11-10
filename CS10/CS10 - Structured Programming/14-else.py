squirrels = 100
trees = 100
bushes = 100

#trees and squirrels
if trees > squirrels:
    print("Let the squirrels live in the tree.")

elif trees < squirrels:
    print("There are not enough trees for the squirrels")

else:
    print("I don't know yet.")

#bushes and trees
if bushes > trees:
    print("We have too many bushes.")

elif bushes < trees:
    print("Maybe they should live in the bushes.")

else:
    print("I still can't decide.")

#squirrels and bushes
if squirrels > bushes:
    print("Yes. Bushes it is!")

else:
    print("Maybe the squirrels should find somewhere else to live.")

#comments
"""The elif conditional statement is a combination of 'else' and 'if'.
When the 'if' or first statment isn't true, the program will move onto elif next to check if its true or not.
This allows for the code to check for multiple condition statements"""

"""The else statement is also a conditional statment that will run if all of the previous statments are false.
This is usually at the end of a if-else sequence, and has no requirements/conditions meaning that if everything is false, then this code will run
For example, the amount of squirrels doesn't have to be less or greater in order for this code to run."""

"""To get the output of 'There are not enough trees for the squirrels, we have too many bushes, and yes. Bushes it is.', we have to fufill the conditions above.
The amount of trees has to be less then the amount of squirrels, the amount of bushes has too be greater then trees, and the amount of squirrels has to be greater then bushes
This would look like trees (80) < bushes (100)< squirrels (120). """

"""To get the output of 'I don't know yet, I still can't decide, and Maybe the squirrels should find somewhere else to live.',
all the pre-existing conditions (if and elif) have to be false.
This means that the program will automatically move onto the else statement and print it out, regardless of what the numbers are.
Since the previous statements are only accounting for greater than and less than each other, then turning the variables into the same number or something that is equal to eachother works
squirrels (100) == trees (100) == bushes (100)"""

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


