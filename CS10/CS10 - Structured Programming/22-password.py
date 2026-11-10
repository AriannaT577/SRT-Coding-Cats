password = "password"
new_password = ""

while(password != new_password):
    print("Please enter your password!")
    new_password = input()
    if (password != new_password):
        print("Incorrect password. Please try again.")

print("Thank you. Your password was entered successfully. ")
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

#1. In what ways are while loops and if statements similar?
    #While loops and if statments are similar, as they both are conditional statments where the condition has to be TRUE in order for the code underneath to run, and FALSE conditions will not run the code
    #For WHILE loops, when the condiditon is TRUE, the code will infinitely run untill the condition is FALSE or BREAK is written
    #For if statments, when the condition is TRUE, the code will run once. If the condition is FALSE, the code will not run and rather move to the next line of code (ELIF, ELSE)

#2. In what ways are while loops and if statements different?
    #They are different, as IF statments only run once, and WHILE loops untill the condition is FALSE (or BREAK)

#3. What is the != represent?
    #!= represents the "does not equal to". This can be used similarly to "varible not (condition)"
