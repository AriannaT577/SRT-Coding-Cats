#kindness
room = 0
move = ""
quizready = False
map1 =("Fun fact of this room: Science supports kindness, as studies show that acts of kindness release oxytocin, sometimes called the \
\"love hormone,\" which boosts happiness and reduces stress.\
\n\nThis is your current position (You are the ##)\n(Reminder, you can leave at anytime by typing \"leave\"):\
\n -----  -----  ----- \n|      |      |     |\n|  ##  |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- ")
quiz1 = False

map2 =("Fun fact of this room: Being kind to youself is one of the most important aspect of all, \
and is the one that gets overlooked often. You need to love and take care of your own mind and body \
before you can be truly ready to give wholeheartedly to others. You cannot pour from an empty cup.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |  ##  |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- ")
quiz2 = False
 
map3 =("Fun fact of this room: World Kindness Day promotes random acts of kindness.\
 One easy way to celebrate World Kindness Day is to carry out one random act of kindness, which can be as simple as complimenting someone or giving a helping hand!\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |  ## |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- ")
quiz3 = False

map4 =("Fun fact of this room: Kindness Week came into being when several humanitarian groups \
came together on November 13, 1997, and made a Declaration of Kindness.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|  ##  |      |     |\n|      |      |     |\
\n -----  -----  ----- ")
quiz4 = False

map5 =("This is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |  ##  |     |\n|      |      |     |\
\n -----  -----  ----- ")#starting position
map5andahalf =("This room is the starting room.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |  ##  |     |\n|      |      |     |\
\n -----  -----  ----- ")

map6 =("Fun fact of this room: However it may appear on the surface, even if they seem fine, you may never truly know what someone else is experiencing. \
That’s why it’s important to be kind to everyone with genuine compassion, some support or a listening ear.\
\n\nThis is your current position (You are the ##)\n(Reminder, you can leave at anytime by typing \"leave\":\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |     |\n|      |      |  ## |\n|      |      |     |\
\n -----  -----  ----- ")
quiz6 = False


print("Hello! Are you ready to explore the depths of Kindness Week? (yes/no)")
ready = input()
if ready == "yes":
    print('You wake up to find yourself in a cloudlike dream, surrounded by fluffy walls.\
\n\nInfront of you, a tiny fairy smiles at you and says, \
"Welcome to the Kindness Space! Here, you can explore each room to learn more about kindness week, its background, and some fun facts! \
To exit this dream, you can type "leave" at anytime. Good luck!"\
\n\nIn front of you is a map that marks your position in the Kindness Space.')
    room = 5
    ready2 = True
    while ready2 == True:
        while move == "leave":
            print("Hope you enjoyed your stay at the Kindness Space!")
            ready2 = False
            break
        while room == 1:
            quiz1 = True
            print(map1)
            print("Where do you want to go? To the right or downwards? (right/down)")
            move = input()
            if move == "right":
                room = 2
            elif move == "down":
                room = 4
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")

        while room == 2:
            quiz2 = True
            print(map2)
            print("Where do you want to go? To the left, right or downwards? (left/right/down)")
            move = input()
            if move == "left":
                room = 1
            elif move == "right":
                room = 3
            elif move == "down":
                room = 5
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")

        while room == 3:
            quiz3 = True
            print(map3)
            print("Where do you want to go? To the left, or downwards?(left/down)")
            move = input()
            if move == "left":
                room = 2
            elif move == "down":
                room = 6
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")

        while room == 4:
            quiz4 = True
            print(map4)
            print("Where do you want to go? To the right, or upwards?(right/up)")
            move = input()
            if move == "right":
                room = 5
            elif move == "up":
                room = 1
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")
    
        while room == 5:
            print(map5andahalf)
            print("Where do you want to go? To the left, right, or upwards?(left/right/up)")
            move = input()
            if move == "left":
                room = 4
            elif move == "up":
                room = 2
            elif move == "right":
                room = 6
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")
        while room == 6:
            quiz6 = True
            print(map6)
            print("Where do you want to go? To the left or upwards? (left/up)")
            move = input()
            if move == "left":
                room = 5
            elif move == "up":
                room = 3
            elif move == "leave":
                print("Hope you enjoyed your stay at the Kindness Space!")
                ready2 = False
                break
            else:
                print("Sorry your move doesn't work here! Try Again.")
    
else:
    print("Come back when your ready!")
