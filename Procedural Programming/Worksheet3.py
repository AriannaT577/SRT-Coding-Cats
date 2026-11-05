#loopity loops
for i in range (10):
    print("Arianna")
print ("Done")

#redgoldredgold
for i in range (20):
    print("Red")
    print("Gold")

#even numbers
for i in range(2,102,2):
    print(i)

#kaboom
count = 10
while count != -1:
    print(count)
    count = count - 1
print ("Blast Off!! Boom!!")

#5. There are three things wrong with this program. List each. (3 pts)
#print("This program takes three numbers and returns the sum.")
#total = 0
#for i in range(3):
#    x = input("Enter a number: ")
#    total = total + i
#print("The total is:", x)

#it only returns the last inputted number not sum
#adding is wrong only adding the in range plus 0
#entering a string not a integer haha (i made the same mistake ngl)

#numbersss
number = 1
while number <11:
    print (number) 
    number = number + 1

#fancy smancy 
positive8 = 0
negative8 = 0
sum8 = 0
zero8 = 0
for i in range(7):
    no8 = int(input("Enter a number:"))
    if no8 > 0:
        positive8 += 1
        sum8 = sum8 + no8
    elif no8 < 0:
        negative8 +=1
        sum8 = sum8 + no8
    else:
        zero8 +=1

print("Total Postitive Enteries:", positive8)
print("Total Negative Enteries:", negative8)
print("Total Zero Enteries:", zero8)
print("Sum of Enteries:", sum8)

#coin tos! gamblining maxing
import random
heads = 0
tails = 0
countcoin = 0

while countcoin < 50:
    flip = random.randint(0, 1)

    if flip == 0:
        print("Heads")
        heads += 1
        countcoin += 1
    else:
        print("Tails")
        tails += 1
        countcoin += 1


print("\ntotal heads:", heads)
print("total tails:", tails)

#rock paper sciessors
print("\nEnter your choice:\n1 = rock\n2 = paper\n3 = scissorcs")

choice10 = int(input("oyur choice: "))
computer = random.randint(0, 2)
if computer == 0:
    computer_choice = "Rock"
elif computer == 1:
    computer_choice = "Paper"
else: #aka if its 2
    computer_choice = "Scissors"

if choice10 == 1:
    user_choice = "Rock"
elif choice10 == 2:
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print("u chose:", user_choice)
print("i chose:", computer_choice)

if user_choice == computer_choice:
    print("tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("boo u win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("boo u win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("boo u win!")
else:
    print("hehe i win!")





