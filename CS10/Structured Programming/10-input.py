print("Hello! What is your age?")
age = input()
#input is a fuction that allows the user to input/personally type in a value that gets stored as a variable
#this can be useful in situations where the user is unable to directly edit the code to change the variables
#can be evident in something such as a survey

days= float(age)*365.25
hours = float(days)*24.0
minutes = float(hours)*60.0
seconds = float(minutes)*60.0

print("You are "+age+" years old? Wow!")
print("Did you know that is around "+str(days), "days?")
print("And wowie, thats over "+ str(hours)+ " hours! Thats a long time!")
print("Or about an impressive "+str(minutes)+" minutes!")
print("Thats also around "+str(seconds)+ " seconds!! Very cool right?")


#logo
print("\n         /\\\\\
\n        // \\\\\
\n       //___\\\\\
\n      //-----\\\\             __________\
\n     //       \\\            ----||----\
\n    /          \\         ---    ||\
\n   /         ___\\_____---       ||\
\n  /                             ||\
\n /       o                      ||\
\n/             \'     o           || ")
