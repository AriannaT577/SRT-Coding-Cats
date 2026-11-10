score = 0

print("Welcome to a simple 3-question geography quiz! \nAre you ready to start? (Y/N)")
ready = input()
if ready == "Y":
    
    print("Great! First question, how many continents are there in the world?")
    print(" A.7\n B.12\n C.1\n D.3")
    print("Choose your answer as A/B/C/D")
    question1 = input()
    if question1 == "A":
        print("That correct!!")
        score += 1 #The plus-equal, which adds to an existing variable (score = score + 1)
    elif question1 == "C":
        print("Incorrect, maybe 300 million years ago though!")
    else:
        print("Incorrect, not quite")
    print()

    print("Second question! What is the tallest mountain in the world?")
    print(" A. Mount Kilimanjaro\n B. Mount Logan\n C. Mount Everest\n D. Mount Fuji")
    print("Choose your answer as A/B/C/D")
    question2 = input()
    if question2 == "C":
        print("Thats correct!!")
        score += 1
    elif question2 == "B":
        print("Incorrect, however Mount Logan is the tallest in Canada!")
    else:
        print("Incorrect, your a little off the mark")
    print()

    print("Last question, which of the following is one of the 5 major oceans?")
    print(" A. The American Ocean\n B. The Artic Ocean\n C. The European Ocean\n D. The Deep Ocean")
    print("Choose your answer as A/B/C/D")
    question3 = input()
    if question3 == "B":
        print("Thats correct!!")
        score += 1
    elif question3 == "D":
        print("Incorrect, all oceans are deep! 90% of them are unexplored!")
    else:
        print("Incorrect, sorry that isn't right")
    print()

    percent = (score*0.3333)*100
    print("Your final score is ",str(score),". That is",str(percent),"%!!")
    if score == 0:
        print("Good effort! Maybe try studying a few more maps...")
    elif score == 1:
        print("Nice job! It could be worse.")
    elif score == 2:
        print("Wow! Your good at geography!")
    elif score == 3:
        print("Perfect score! What a geography genius!")
    else:
        print("Umm this shouldn't be possible. How did you-")
    print()
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

elif ready == "N":
    print("Come back when your ready!")
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
    print("I'm a little confused...try again!")
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
