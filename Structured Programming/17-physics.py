print("Welcome to the super cool formula caluculator! \nChoose the formula you want to solve below:")
print(" 1. Newton's second law (F=m*a)\n 2. Area of a parallelogram (A = b * h)")
print("Please type in either 1 or 2")
formula = input()

if formula == "1":
    print("You have selected Newton's second law! Please type in the values for force, mass, and acceleration. For the unknown variable that you wish to solve for, type in '?'")
    print("Force (F):")
    force = input()
    print("Mass (m):")
    mass = input()
    print("Acceleration (a):")
    acceleration = input()
    if force == "?":
        answer = float(mass)*float(acceleration)
    elif mass == "?":
        answer = float(force)/float(acceleration)
    elif acceleration == "?":
        answer = float(force)/float(mass)
    print("Your answer is",str(answer),"! Thank you for using the super cool formula caluculator!")

elif formula == "2":
    print("You have selected Area of a parallelogram! Please type in the values for area, base or height. For the unknown variable that you wish to solve for, type in '?'")
    print("Area (A):")
    area = input()
    print("Base (b):")
    base = input()
    print("Height (h)")
    height = input()
    if area =="?":
        answer = float(base)*float(height)
    elif base == "?":
        answer = float(height)/float(area)
    elif height == "?":
        answer == float(base)/float(area)
    print("Your answer is",str(answer),"! Thank you for using the super cool formula caluculator!")
else:
    print("Sorry, I'm confused. Try again later")
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
    
