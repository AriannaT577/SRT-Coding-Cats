#1. 
#boolean, true/false
#int, whole numbers
#string, like text n stuff
#float, decimals

#2
my_list = [5, 2, 6, 8, 101]
print(my_list[1])
print(my_list[4])
#print(my_list[5])
#this code prints the list stated above. it will print
#the 1st number on the list, 2 (starts from 0), then 101 (4th number)
#then it will have an error as there is no 5th number in the list

#3
#What does this code print out?
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
#this code prints out the list in each line in order

#4
#What does this code print out?
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
#my_list2[2] = 10
print(my_list2)
#the first part of the code prints out the list of stuff. however
#in both lists some numbers are replaced as 10. in the first lists, 
#since the brackets are square, its tuple (?) which means u can change
#the items in the list. however, for the second list its not as the 
#brackets are rounded which means u cant change things, causing an 
#error to pop up

#5 What does this code print out?
my_list = [3 * 5]
print(my_list)
#this one, since its in the brackets to get the value, u do the math
#and print the list, which in this case is [15]
my_list = [3] * 5
print(my_list)
#for this one, since the x5 is outside of the brackets, it repeats
#the list 5 times, printing something like [3, 3, 3, 3, 3]

#6 What does this code print out?
my_list = [5] 
for i in range(5):
    my_list.append(i)
print(my_list)
#the for i in range append dictates the range of the append
#which means from 5, it will go backwards 4, 3, 2, 1, 0
#printing [5, 0, 1, 2, 3, 4]

#7. What does this code print out?
print(len("Hi"))
print(len("Hi there."))
print(len("Hi") + len("there."))
print(len("2"))
#print(len(2))
#this code prints out len, which is the amount of charactera
#in each line. "Hi" has 2 characters, "Hi there." has 9, etc
#however the last one is a int, and you can only use 'len'
#for string types, not int types

#8. What does this code print out?
print("Simpson" + "College") #simpsoncollege, js putting the two together
print("Simpson" + "College"[1]) #it prints simpson, then the 1
#letter of college, which is o, printing Simpsono
print( ("Simpson" + "College")[1] ) #it adds the whole thing together
#then it prints the 1st letter of the whole thing, which is just i

#9. What does this code print out?
word = "Simpson"
for letter in word:
    print(letter)
    #in every line it prints each letter in the word, aka like 
    #S
    #I
    #M
    #P
    #S
    #O
    #N

#10. What does this code print out?
word = "Simpson"
for i in range(3):
    word += "College"
print(word)
#since it added the word college each line three times, its gonna 
#simpson
#simpsoncollege
#simpsoncollegecollege
#in a staircase bc its like adding it over time, 3 times in the loop

#11. What does this code print out?
word = "Hi" * 3
print(word)
#it prints hi three times, HIHIHIHI

#12. What does this code print out?
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
#in the sentence, it prints the 3 spot which would be a space " "
print("The -1 spot is: " + my_text[-1])
#in the sentence, it prints the -1 spot which loops around 
#and prints "." at the end of the sentence

#13. What does this code print out?
s = "0123456789"
print(s[1]) #prints the first number [1]
print(s[:3]) #prints everything before the 3rd number [012]
print(s[3:]) #print everything after the 3rd number [3456789]

#14. Write a loop that will take in a list of five numbers from the user,
#adding each to an array. Then print the array. 
#Try doing this without looking at the book.
numbers = []
for i in range(5):
    num = int(input("number: "))
    numbers.append(num)
print("list is:", numbers)

#15. Write a program that take an array like 
# the following, and print the average. 
# Use the len function, don't just use 15, because that won't work if
# the list size changes.
# (There is a sum function I haven't told you about. Don't use that.
# Sum the numbers individually as shown in the chapter.)
# (Also, a common mistake is to calculate the average each time
# through the
# loop to add the numbers. Finish adding the numbers before you
# divide.)
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
total = 0
for number in my_list:
    total = total + number
average = total / (len(my_list))
print (average)
