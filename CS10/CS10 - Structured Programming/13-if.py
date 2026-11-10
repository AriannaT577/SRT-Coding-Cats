print("What do you think you can do legally? Lets test!\nFirst, whats your name?")
name = input()
print("Great",name,"! Now, How old are you?")
age = int(input())

if age < 16:
    print("Aw man, sorry",name,", you can't drive either.")

if age < 18:
    print( "Unfortunately",name,", you can't vote.")

if age < 25:
    print("Sorry",name,"you can't rent a car.")

if age >= 25:
    print( "Great",name,"! You can do anything that's legal!")
