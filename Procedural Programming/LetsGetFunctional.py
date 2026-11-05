#1 - function called min 3 that returns smallest number
def min3(a, b, c):
    if a <= b and a <= c: #if a is less then b and c aka smallest
        return a
    elif b <= a and b <= c: #if b is smallest
        return b
    else:
        return c #if b and a are greater then c (c is smallest)
print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

#2 - creating box function
def box (l, w):
    for i in range (l): #length aka like height of box
        print("*" * w) #width aka like how much across
box(7,5)
print()
box(3,2)
print()
box(3,10)

#3 - finding stuff in a list
def find(my_list3, key):
    for i in range(len(my_list3)):
        if my_list3[i] == key:
            print(f"Found {key} at position {i}")
my_list3 = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
find(my_list3, 12)
find(my_list3, 91)
find(my_list3, 80)

