counter = 0

print ("Please respond by answering either T for True or F for False")
print ('The purpose of this program is for you to understand the "and" and "or"\ncompound conditional statements.')
print()
while counter < 12:
    if counter == 0:
        answer_one = input("(5 >= 4) and (1 == 1): ")
        if answer_one == "T":
            print("Correct! Moving on to question 2!")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0
    
    if counter == 1:
        answer_two = input("(5 == 4) and (7 < 8): ")
        if answer_two == "F":
            print("Correct! Question 3")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 2:
        answer_three = input("(25 <= 24) or (11 == 11): ")
        if answer_three == "T":
            print("Correct! Question 4")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 3:
        answer_four = input("(-7 > -6) and (100 > 50): ")
        if answer_four == "F":
            print("Correct! Question 5")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 4:
        answerFive = input("(-9 == 9) or (40 > 30): ")
        if answerFive == "T":
            print("Correct! Question 6")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 5:
        answer_six = input("(7 == 8) or (1 > 0): ")
        if answer_six == "T":
            print("Correct! Question 7")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 6:
        answer_seven = input("not(7 > 6) and (1 == 1): ")
        if answer_seven == "F":
            print("Correct! Question 8")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 7:
        answer_eight = input("TRUE and FALSE: ")
        if answer_eight == "F":
            print("Correct! Question 9")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 8:
        answer_nine = input("TRUE or FALSE: ")
        if answer_nine == "T":
            print("Correct! Question 10")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 9:
        answer_ten = input("not(TRUE and TRUE) or not(FALSE and TRUE): ")
        if answer_ten == "T":
            print("Correct! Question 11")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0
#the two more questions
    if counter == 10:
        answer_eleven = input("False and False: ")
        if answer_eleven == "F":
            print("Correct! Question 12")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 11:
        answer_twelve = input("not (True and False) or 0 == 26: ")
        if answer_twelve == "T":
            print("CONGRATULATIONS! You have completed the compound conditional quiz.")
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
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    
        

"""
1. What are the logic rules to the 'and' compound condition?
    When using 'and', this means that both conditions have to be true in order for the statement to be true. Even if one of them is true, the other has to be true otherwise the statement is considered false.
    This can been seen in question 4, ("(-7 > -6) and (100 > 50): "). Here, although 100 is greater then 50, (-7) is not greater then (-6), therefore the entire statement is false.

2. What are the logic rules to the 'or' compound condition?
    When using the 'or' condition, this allows for there to be multiple conditions that will allow the statement to be true, without requiring them to all be true like using 'and'.
    This can be seen in question 3, ("(25 <= 24) or (11 == 11): "). Although 25 is not less then 24 (and therefore false), 11 is 11 which makes the entire condition/statement true. 

3. What do you think the += operation does?
    The '+=' operation allows the user to adds to a variable without knowing the variable. It is the same as "variable = (variable)+1". Using this, you don't have to know the variable beforehand,
    allowing you to use it for something like a quiz, where you dont know what the score is (as the user could have gotten it right or wrong). Using this rather than the long statement
    also makes the code significantly easier and efficient. 

4. Why do you think that the program will loop when you get a question incorrect?
    The program loops when a question is incorrect because it sets the counter to 0, rather then + or - anything. The code is dependent on the counter, as the counter is what allows the program
    to know what question you are on. When the counter is 0, it resets to the beginning since the code is running the "if counter = 0:" statment at the begining as the counter is reset to 0.

"""
        
    
