import random
from random import randint
escape= False
death = 0
topL =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|  XX  |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter1 = False

map2 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |  XX  |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter2 = False

map3 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |    XX    |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter3 = False

map4=("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|    XX   |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter4 = False

map5 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         | XX|----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter5 = False

map6 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|  XX  |      |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter6 = False
code = "FPOB"
hammer = False

map7 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |  XX  |     |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter7 = False

map8 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      | XX  |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter8 = False

map9 =("This is your current position marked on a map you found beside you:\
\n -----  -----  ---------- \n|      |      |          |\n|      |      |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      |     |  XX |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----")
enter9 = False

print("Lets go on an adventure!")
print("\nAfter getting fired on the first day of your job, you tragically get kidnapped.\nWhen you wake up, you find yourself in a building with 9 rooms. \
\nYou decide to navigate them, however you are tired and may pass out. Try to escape with only moving around 20 times!\n")
room = randint (1,9)
while escape == False:
    while room == 1:
        death+= 1
        enter1 = True
        print("\nYou enter a crusty room with many pictures and posters on the wall, extending to the room beside you. By the looks of it, they are a collection of cat memes.\
\nFrom left to right, the cat names are Floppa, Pop Cat, OIIA Cat, and Bingus.")
        print(topL)
        print("Where do you want to go? To the right or down? (right/down)")
        move = input()
        if move == "right":
            room = 2
        elif move == "down":
            room = 4
        else:
            print("Sorry your move doesn't work here! Try Again.")

    while room == 2:
        death+= 1
        enter2 = True
        print("\nYou enter a musty room with many poster and catmemes on the wall, extending to the room beside you.\
On the ground infront of you, you see a map with a red pen circling the bottom second to the left room.")
        print("You are the 'XX', the circled room is the '00':\
\n -----  -----  ---------- \n|      |      |          |\n|      |  XX  |          |\n|      |      |          |\
\n --------  ---           |\n|         |   |          |\n|         |   |----------\n|         |   |\
\n -----  -----  ----- ----- \n|      |      |     |     |\n|      |      | 00  |     |\n|      |      |     |     |\
\n|      |      |     |     |\
\n -----  -----  ----- -----\n")
        print(map2)
        print("Where do you want to go? To the left, right or down? (left/right/down)")
        move = input()
        if move == "left":
            room = 1
        elif move == "right":
            room = 3
        elif move == "down":
            room = 5
        else:
            print("Sorry your move doesn't work here! Try Again.")
    
    while room == 3:
        death+= 1
        print("\nYou enter the big top rightmost room. In this room, you see jail-like bars on the far side of the room, looking like a dungeon.\
In suspiciously red writing, the walls say \"Run! Get outta here! Don't let the cult find you!\"")
        enter3 = True
        print(map3)
        print("Where do you want to go? Note that you can only go left, however there is an upper and lower room.\
Do you want to go to the upper room (type \"up\") or the lower hallway (type \"down\"? (up/down)")
        move = input()
        if move == "up":
            room = 2
        elif move == "down":
            room = 5
        else:
            print("Sorry your move doesn't work here! Try Again.")
    
    while room == 4:
        death+= 1
        enter4 = True
        print("\nThis room looks like a plain boring room. How lame.")
        print(map4)
        print("Where do you want to go? To the right, up or down? (right/up/down)")
        move = input()
        if move == "right":
            room = 5
        elif move == "up":
            room = 1
        elif move == "down":
            room = 6
        else:
            print("Sorry your move doesn't work here! Try Again.")
            
    while room == 5:
        death+= 1
        enter5 = True
        print("\nYou enter the long hallway. It looks damp and creepy, like in a horror movie.\
You can go in four directions, with a suspiciously red stain on the ground with drag marks towards the room directly south and downwards. ")
        print(map5)
        print("Where do you want to go? To the left, right, up or down? (left/right/up/down)")
        move = input()
        if move == "left":
            room = 4
        elif move == "right":
            room = 3
        elif move == "up":
            room = 2
        elif move == "down":
            room = 7
        else:
            print("Sorry your move doesn't work here! Try Again.")

    while room == 6:
        death+= 1
        enter6 = True
        print(map6)
        if hammer == False:
            print("\nYou enter the bottom leftmost room. In this room, you see a chest with a four letter lock.")
            if enter1 ==  True:
                print("You recall the top left room had a series of posters of cat memes, with the names of Floppa, Pop Cat, OIIA Cat, and Bingus.\
Perhaps you can try the first letters of each cat memes?")
            print("You can try opening the chest, or go to another room. Which do you want to do? Please type 'chest' or 'move'.")
            input6 = input()
            while input6 == "chest":
                print("Please type what you think the code is. The Format is ABCD, all capitals and no spaces:")
                input6half = input()
                if input6half == code:
                    print("Wow! You guessed the code. The chest opens up and you see a hammer inside. Must be useful for later!")
                    hammer = True
                    input6 = "move"
                else:
                    print("Yikes, that doesn't seem like the correct code. Try moving to different rooms to find hints.\
Do you want to try again? Type \"chest\" to try again, or \"move\" to exlpore more rooms. ")
                    input6 = input()
            else:
                print("\nYou either chose move, or nothing. If what you chose is invalid and you would like to try inputting the code, re-enter the room to attempt.")
        if hammer == True:
             print("\nYou enter the bottom leftmost room. You have already entered the room this room and collected the hammer.")
        print("Where do you want to go? To the right or up? (right/up)")
        move = input()
        if move == "right":
            room = 7
        elif move == "up":
            room = 4
        else:
            print("Sorry your move doesn't work here! Try Again.")

    while room == 7:
        death+= 1
        enter7 = True
        print("\nYou enter the bottom room adjacent to the hallway. It doesn't have any items of significance.\
However, you can see writing on the walls saying: \"Praise the Cat Cult!\". How peticular...")
        print(map7)
        print("Where do you want to go? Note that you cannot enter the leftmost room in the middle row.\
Going up will bring you into the hallway. To the left, right or up? (left/right/up)")
        move = input()
        if move == "left":
            room = 6
        elif move == "right":
            room = 8
        elif move == "up":
            room = 5
        else:
            print("Sorry your move doesn't work here! Try Again.")

    while room == 8:
        death+= 1
        enter8 = True
        print("You enter a well furnished room. You also notice an exit! However, it appears to be boarded up with some wooden planks. \
\nYou may be able to escape by finding something to take it off. ")
        if hammer == True:
            print("Where do you want to go? Note that you can escape by typing hammer")
        print(map8)
        print("Where do you want to go? To the left or right? (left/right)")
        move = input()
        if move == "left":
            room = 7
        elif move == "right":
            room = 9
        elif move == "hammer":
            escape = True
            break
        else:
            print("Sorry your move doesn't work here! Try Again.")

    while room == 9:
        death+= 1
        enter9 = True
        print("The bottom right most room of the building. Its fairly plain, and looks abandoned. Nobody has probably entered it in a long time, ")
        print(map9)
        print("Where do you want to go? Note that you are unable to go to go in any direction but right. \
To the right? (right)")
        move = input()
        if move == "right":
            room = 8
        else:
            print("Sorry your move doesn't work here! Try Again.")
else:
    print("Come back when your ready!")
    
while escape == True:
    if death <= 15:
        print("You escaped yipee!")
