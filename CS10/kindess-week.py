#kindess
room = 0
escape = False
move = ""
quizready = False
map1 =("Room 1:\nFun fact of this room: Science supports kindess, as studies show that acts of kindness release oxytocin, sometimes called the \
\"love hormone,\" which boosts happiness and reduces stress.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|  ##  |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|      |      |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")
quiz1 = False
unlocked1=("Room 1:\nFun fact of this room: Science supports kindess, as studies show that acts of kindness release oxytocin, sometimes called the \
\"love hormone,\" which boosts happiness and reduces stress.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|  ##  |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |QUIZ |\n|      |      |ENTRY|\n|      |      |OPEN |\
\n -----  -----  ----- ")

map2 =("Room 2:\nFun fact of this room: Being kind to youself is one of the most important aspect of all, \
and is the one that gets overlooked often. You need to love and take care of your own mind and body \
before you can be truly ready to give wholeheartedly to others. You cannot pour from an empty cup.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |  ##  |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|      |      |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")
quiz2 = False
unlocked2 =("Room 2:\nFun fact of this room: Being kind to youself is one of the most important aspect of all, \
and is the one that gets overlooked often. You need to love and take care of your own mind and body \
before you can be truly ready to give wholeheartedly to others. You cannot pour from an empty cup.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |  ##  |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |QUIZ |\n|      |      |ENTRY|\n|      |      |OPEN |\
\n -----  -----  ----- ")

map3 =("Room 3:\nFun fact of this room: World Kindness Day promotes random acts of kindness.\
 One easy way to celebrate World Kindness Day is to carry out one random act of kindness, which can be as simple as complimenting someone or giving a helping hand!\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |  ## |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|      |      |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")
quiz3 = False
unlocked3 =("Room 3:\nFun fact of this room: World Kindness Day promotes random acts of kindness.\
 One easy way to celebrate World Kindness Day is to carry out one random act of kindness, which can be as simple as complimenting someone or giving a helping hand!\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |  ## |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |QUIZ |\n|      |      |ENTRY|\n|      |      |OPEN |\
\n -----  -----  ----- ")

map4 =("Room 4:\nFun fact of this room: Kindness Week came into being when several humanitarian groups \
came together on November 13, 1997, and made a Declaration of Kindness.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|  ##  |      |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")
quiz4 = False
unlocked4 =("Room 4:\nFun fact of this room: Kindness Week came into being when several humanitarian groups \
came together on November 13, 1997, and made a Declaration of Kindness.\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |QUIZ |\n|  ##  |      |ENTRY|\n|      |      |OPEN |\
\n -----  -----  ----- ")

map5 =("This is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|      |  ##  |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")#starting position
map5andahalf =("This room is the starting room. Go to all the other rooms to unlock the quiz!\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |\\   /|\n|      |  ##  |  X  |\n|      |      |/   \\|\
\n -----  -----  ----- ")
unlocked5 =("This room is the starting room. Go to the quiz room to exit the dream!\
\n\nThis is your current position (You are the ##):\
\n -----  -----  ----- \n|      |      |     |\n|      |      |     |\n|      |      |     |\
\n -----  -----  ----- \n|      |      |QUIZ |\n|      |  ##  |ENTRY|\n|      |      |OPEN |\
\n -----  -----  ----- ")


print("Hello! Are you ready to explore the depths of Kindness Week? (yes/no)")
ready = input()
if ready == "yes":
    print('You wake up to find yourself in a cloudlike dream, surrounded by fluffy walls.\
\n\nInfront of you, a tiny fairy smiles at you and says, \
"Welcome to the Kindness Space! Here, you can explore each room to learn more about kindness week, its background, and some fun facts! \
To exit this dream, visit all rooms and complete the quiz at the end! That room is marked on the map, and is only unlocked once you visit all rooms. Good luck!"\
\n\nIn front of you is a map that marks your position in the Kindness Space.')
    room = 5
    ready2 = True
    while ready2 == True:
        if quiz1 == True and quiz2== True and quiz3 and quiz4 == True:
            quizready = True
        while room == 1:
            quiz1 = True
            if quiz1== True and quiz2== True and quiz3== True and quiz4 == True:
                quizready = True
                print(unlocked1)
                print("Where do you want to go? To the right or down? (right/down)")
                move = input()
                if move == "right":
                    room = 2
                elif move == "down":
                    room = 4
                else:
                    print("Sorry your move doesn't work here! Try Again.")
            else:
                print(map1)
                print("Where do you want to go? To the right or down? (right/down)")
                move = input()
                if move == "right":
                    room = 2
                elif move == "down":
                    room = 4
                else:
                    print("Sorry your move doesn't work here! Try Again.")

        while room == 2:
            quiz2 = True
            if quiz1== True and quiz2== True and quiz3== True and quiz4 == True:
                quizready = True
                print(unlocked2)
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
            else:
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
            quiz3 = True
            if quiz1== True and quiz2== True and quiz3== True and quiz4 == True:
                quizready = True
                print(unlocked3)
                print("Where do you want to go? To the left, or down? Note that downwards is the quiz room to exit!(left/down)")
                move = input()
                if move == "left":
                    room = 2
                elif move == "down":
                    room = 6
                else:
                    print("Sorry your move doesn't work here! Try Again.")
            else:
                print(map3)
                print("Where do you want to go? Unfortunely, you can only go left as you haven't unlocked the quiz room yet!(left)")
                move = input()
                if move == "left":
                    room = 2
                elif move == "down":
                    print("Sorry! You don't have access to this room.")
                    print("Where do you want to go? Unfortunely, you can only go left as you haven't unlocked the quiz room yet!(left)")
                    move = input()
                else:
                    print("Sorry your move doesn't work here! Try Again.")

        while room == 4:
            quiz4 = True
            if quiz1== True and quiz2== True and quiz3== True and quiz4 == True:
                quizready = True
                print(unlocked4)
                print("Where do you want to go? To the right, or upwards?(right/up)")
                move = input()
                if move == "right":
                    room = 5
                elif move == "up":
                    room = 1
                else:
                    print("Sorry your move doesn't work here! Try Again.")
            else:
                print(map4)
                print("Where do you want to go? To the right, or up?(right/up)")
                move = input()
                if move == "right":
                    room = 5
                elif move == "up":
                    room = 1
                else:
                    print("Sorry your move doesn't work here! Try Again.")
    
        while room == 5:
            if quiz1== True and quiz2== True and quiz3== True and quiz4 == True:
                quizready = True
                print(unlocked5)
                print("Where do you want to go? To the left, right, or up? Note that going right will let you take the quiz and exit the Kindess Space!(left/right/up)")
                move = input()
                if move == "left":
                    room = 4
                elif move == "up":
                    room = 2
                elif move == "right":
                    room = 6
                else:
                    print("Sorry your move doesn't work here! Try Again.")

            else:
                print(map5andahalf)
                print("Where do you want to go? To the left, or up?(left/up)")
                move = input()
                if move == "left":
                    room = 4
                elif move == "up":
                    room = 2
                elif move == "right":
                    print("Sorry! You don't have access to this room.")
                    print("Where do you want to go? To the left, or up?(left/up)")
                    move = input()
                else:
                    print("Sorry your move doesn't work here! Try Again.")
                    
        while room == 6:
            print("Welcome to the quiz room! After you complete the quiz, you will prove yourself to be kind and you will exit the dream!")
            score = 0
            question_1 = input("1. What does kindness release?\
\n A. oxygen\
\n B. oxytocin\
\n C. hydrogen\
\n D. metabolism \
\n Please choose an option (A/B/C/D):\n")

            if(question_1 == "B"):
               print("\n")
               print("Correct!") 
               score += 1
            else:
               print("\nIncorrect.\n")
               
            question_2 = input("2. Is being kind to others the only important aspect of being kind? (true/false)?\n")
            if question_2 == "false":
                print("\n")
                print("Correct!")
                score += 1
            else:
                print("\nIncorrect.\n")
    
            question_3 = input("3.Of which type of group came together to make the Declaration of Kindness?\n\
\n A. Social\
\n B. Global\
\n C. Humanitarian\
\n D. Food\
\n Please choose an option (A/B/C/D):\n")

            if(question_3 == "C"):
                print("\n")
                print("Correct!")
                score += 1
            else:
                print("\nIncorrect.\n")

            question_4 = input("2. Is complimenting someone considered an act of kindness? (true/false)?\n")
            if question_4 == "true":
                print("\n")
                print("Correct!")
                score += 1
            else:
                print("\nIncorrect.\n")


            percentage_score = round((score/4) * 100, 2)
            print("Your final score is " + str(score) + "/4. That is " + str(percentage_score) + "%.")
            if score == 4:
                print("Congratulations! You successfully passed the quiz and simultaneously learned about the history of Kindness Week.\
Tomorrow, you will be able to wake up after escaping this dream. Well done!")
                
                room = 0
                break
            else:
                print("I’m sorry. You did not pass the quiz. Try again to escape your dream.")
                        
else:
    print("Come back when you are ready!")
        
            
