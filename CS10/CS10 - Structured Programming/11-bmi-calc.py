#BMI= mass/(height^2)
print("BMI Calculator\
\n-------------------")
print("\nWelcome to the BMI calculator! What is your name?")
name= input()
print("Hello ",name,"! May I know your weight in kilograms?")
weight=float(input())
print("Thank you! Finally, what is your height in meters?")
height=float(input())

bmi= round(float(weight/(height*height)),2)
print("Alright",name,", your BMI is",str(bmi),".")

if bmi <= 18.4:
    print("Your BMI is under 18.4, you are underweight")
elif ((bmi >=18.5) and (bmi <=24.99)):
    print("Your BMI is between 18.5  and 24.99. You are in a normal and healthy range. ")
else:
    print("Your BMI is over 25. You are overweight. I reccomend double checking your diet!")

print("Thank you for time!\n-------------------")

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

