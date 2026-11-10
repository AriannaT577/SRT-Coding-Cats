#Counting using FOR loops
print("Welcome to the Cool-Counting-Program. Are you ready to start?\
 Please type \"Y\" for yes, and \"N\" for no.")
ready = input()

while ready == "Y":
    print("What is the starting number of the counting sequence?")
    start= int(input())
    print("Great! What is the ending number of the counting sequence?")
    end= int(input())
    print("Nice! What is the amount you want to count by in the counting sequence?")
    countamount= int(input())

    if countamount <= 0 or (end - start) % countamount != 0:
        valid = False
    else:
        valid = True

    if valid == True:
        print("This is your counting sequence, with the starting number of", start, ", an ending number of",end," and an amount your counting by of",countamount,".")
        for number in range(start,end+1,countamount):
            print(number)
        print("\nWould like to try again? Type in \"Y\" for yes, and \"N\" for no.")
        ready = input()

    elif valid == False:
        print("Sorry! The amount you are counting by," ,countamount, "is unable to reach your ending number,",end,".\
If you would like to try again, type in \"Y\" for yes, and \"N\" for no.")
        ready = input()
    
else:
    print("Come back later!")
    print("         /\\")
    print("        // \\")
    print("       //___\\")
    print("      //-----\\             __________")
    print("     //       \\            ----||----")
    print("    /          \         ---   ||")
    print("   /         ___\_____---      ||")
    print("  /                            ||")
    print(" /       o                     ||")
    print("/             \'     o          || ")


