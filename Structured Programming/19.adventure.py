print("Welcome to your spooky adventure at Floppa's!\nAre you ready to start? (Y/N)")
ready = input()
bingus = ("⠀⢀⡀⠤⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⣀⡀⠀⡀⢀⠀⢀⣀⠀\
\n⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠤⠤⠐⠂⠈⠉⠉⠁⠉⠈⠀⠉⠈⠁⠉⠀⠉⠈⠉⠀⠒⠀⠤⠤⠐⠂⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄\
\n⢸⠀⠀⠀⢶⣄⡠⠤⠤⠒⠒⠒⠂⠤⠤⠤⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣀⣀⣀⣀⡀⡄⣀⣀⠀⠀⢨⡄\
\n⠸⡆⠀⠀⠈⡇⠈⠁⠀⠀⠓⢦⣀⠀⠀⠀⠀⠀⠀⠙⠢⢄⠀⣀⠤⠔⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠉⠑⠒⠒⠤⠤⠐⠒⠊⠉⠀⠀⠀⠀⡤⣄⡀⣐⣴⡿⠋⠀⠀⢸\
\n⠀⠱⡀⠀⠀⠘⡄⠀⢠⡀⠄⡀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣀⡛⢡⠐⣹⣏⠁⢀⡇⠀⠀⠀⡎\
\n⠀⠀⢳⠀⠀⠀⠘⣤⡈⢣⠘⣴⢻⣾⣤⣰⡀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣯⣶⣿⣿⢡⢆⡙⠄⠻⠶⠞⡇⠀⠀⢘\
\n⠀⠀⠀⢣⠀⠀⠀⣿⠀⢂⠹⣾⣯⢿⣿⣿⣆⠀⣿⡏⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⣿⣿⣷⣯⣷⠌⢂⠀⠀⣰⠃⠀⠀⢸\
\n⠀⠀⠀⠘⡄⠀⠀⠸⣇⠠⠘⢸⣿⣿⣿⠻⣯⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠻⢿⣿⣿⡏⡜⠀⠀⣼⠏⠀⠀⠀⡜\
\n⠀⠀⠀⠀⢣⠀⠀⠀⢻⡄⣱⣾⠟⠋⠀⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠉⠙⠿⣷⣌⣠⠏⠀⠀⠀⡸⠁\
\n⠀⠀⠀⠀⠀⡆⠀⠀⠈⣿⠟⠁⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⣀⣤⣶⣦⣤⡀⠀⠉⢻⡟⠀⠀⠀⡰⠁\
\n⠀⠀⠀⠀⠀⠘⡀⠀⠀⠸⣄⠀⠀⢀⠀⠀⠀⢰⣿⣽⣿⣿⣿⣿⣿⣷⣤⠢⡐⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢄⣲⢇⣶⣿⣿⣿⣿⣿⣾⣿⠀⢠⡾⠀⠀⠀⢰⠃\
\n⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠈⢻⣼⠟⠂⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠂⡜⢀⠂⠀⠀⠀⠀⠀⠀⠠⠈⣄⡞⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⠃⠀⠀⢠⠇\
\n⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠹⣤⠀⠄⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡇⠐⢂⠈⠄⠀⠀⠀⠀⠈⠠⠑⢨⠑⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣿⠀⠀⠀⡸\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠘⣇⠀⠀⢀⠈⢻⣿⠿⣿⣿⣿⣿⣫⣿⣿⡷⠈⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠄⠂⣾⣿⣿⣿⣿⠿⣿⣻⠟⢁⣼⠏⠀⠀⠀⡇\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⠀⠀⠀⣻⠐⠈⠄⡨⠄⡌⢛⠶⠦⠷⠿⠛⠉⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢈⠀⠡⠉⠀⠉⠛⠛⢛⣛⣡⡶⢯⡏⠀⠀⠀⡸\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⢠⡇⠘⡈⠰⣀⢣⠘⡤⢢⠑⡰⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠉⠁⠀⠀⠈⠀⠐⢈⠡⢩⣷⠟⠀⠀⠀⡰⠁\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠈⡇⠰⢈⠡⢂⠦⢩⠔⡡⢊⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣷⠋⠀⠀⠀⡰⠁\
\n⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⡼⢃⠐⠌⢢⠍⣎⠱⣊⠱⡌⡘⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⢫⣽⠃⠀⠀⠀⡐⠁\
\n⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⡼⠁⢈⠐⡈⢆⡉⢆⠳⡌⡓⢬⠑⡌⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠀⠀⡤⢐⠈⣆⣿⠃⠀⠀⠀⡜\
\n⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⣸⢃⠐⠀⠂⠌⢠⠘⡌⡓⢬⡑⢎⡒⠄⢡⠠⢁⠢⠄⡀⢀⠠⣴⡲⢦⡲⢶⡼⣿⣶⢰⡟⢡⡌⢦⡹⣾⠀⠀⠀⡘\
\n⠀⠀⠀⠀⠀⡰⠁⠀⠀⢀⡴⢃⠄⠀⠌⠐⠈⠄⢊⡐⢉⠆⡙⠦⣉⠞⣠⠢⢡⢆⠱⣈⠦⣁⠛⣿⣳⣿⣯⣿⠟⣥⢧⣚⣥⢺⣽⠓⣿⠀⠀⠀⡇\
\n⠀⠀⠀⠀⡰⠁⠀⠀⢀⡾⣑⠈⠀⢈⠠⢁⠢⠌⡄⢌⠢⢌⢡⠓⣬⢚⡤⣛⡴⢪⢵⣘⢦⡝⣺⢴⣻⣿⣿⢣⣟⡞⣧⠿⣜⣿⡎⢧⣹⠀⠀⠀⢹\
\n⠀⠀⠀⡰⠁⠀⠀⢠⢟⠰⠁⠀⠀⠀⠐⡈⠰⠩⢜⢢⠳⡌⢦⡝⢦⣋⠶⣣⢻⡝⣮⡝⣶⣹⢷⣫⣟⡿⣞⡿⣾⡽⣯⢿⣽⢺⡝⢦⡹⡇⠀⠀⠈⡄\
\n⠀⠀⢰⠁⠀⠀⢠⠏⠰⠁⠀⠀⠀⠀⠐⠀⠡⢁⠊⡄⢣⠘⣅⠚⡤⢋⢞⡱⢧⣛⢶⡻⣵⣻⣞⣷⣫⢿⣽⣻⢷⣻⣯⣟⡾⣻⢼⢣⡱⣧⠀⠀⠀⡇\
\n⠀⢀⠇⠀⠀⢀⡾⣸⠁⠀⠀⠀⠀⠀⠀⡀⠁⢂⠐⡈⢄⠣⢄⠋⡴⢉⠦⣙⠶⣹⢞⡽⣳⡽⣞⡾⣽⣻⢾⣽⣻⡽⣾⡽⣳⢏⣟⢦⡑⣿⠀⠀⠀⢸\
\n⠀⣸⠀⠀⠀⣼⢣⡅⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠂⡐⠠⠒⣈⠒⡌⡱⢊⡥⢫⡕⣫⢞⡵⣻⣝⣻⢷⣯⣟⡾⣳⢟⣧⢿⡹⣞⢼⡣⢞⡸⡇⠀⠀⠈⡄\
\n⠀⡇⠀⠀⢈⡯⠽⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠂⠠⢀⠡⠒⣀⠣⢌⡑⠣⡜⡡⢞⡱⢎⡷⣣⢯⣛⡾⣳⠾⣽⡝⣾⢣⣏⢷⡹⣆⠟⡤⢓⣷⠀⠀⠀⢃\
\n⠰⠇⠀⠀⢸⡿⠆⠀⠀⠀⠀⠀⠀⠀⢈⠀⠠⠁⢂⠐⠠⢁⠂⢅⠢⠌⡱⢐⠱⢌⠲⡍⠶⣭⢳⣏⢷⣫⢟⡵⣻⣜⡳⣎⢷⠳⣭⢚⣥⢃⢿⡄⠀⠀⠸⡀")
floppa =("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢻⡇⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀       ⠀⠀⣧⣶⣿⣿⣿⣿⣆⡀\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠿⢿⣿⣿⣿⣇⡀⠀⠀⠀⠀  ⠀⣿⡀⠀⠀⣠⣾⢏⣿⡏⠀⠀⠈⠙⠳\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠁⠀⠀⠀⢹⣿⣿⣽⣿⣦⠀⠀⠀ ⠀⢿⡇⠀⣼⠟⣰⣾⣡⣇\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣿⣿⣧⣀⣀⣀⣸⣇⣼⣿⣠⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⡶⠶⠊⣷⢶⢶⣶⢶⣤⣤⣄⣀⡀\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣮⣿⡿⣿⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⡛⢛⠉⢁⣩⣻⠀⠄⠀⠁⠀⠀⠀⠈⠀⡊⠉⠙⠙\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣇⣾⣿⣧⣿⣿⣿⣿⢿⣇⠀⢀⣀⣤⣶⣿⡷⡿⢻⣵⡯⠙⠀⠀⠀⢋⠁⠀⠀⠀⠀⠀⡀⡀⠀⠀⢠⠂\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣽⣿⣿⡿⢩⣿⣿⣿⣗⣿⣯⣿⣿⣟⣃⠀⢁⣴⣫⣗⡹⠃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠠⠊\
\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣿⣿⣿⣽⠿⣿⣿⣟⣿⠧⣼⡿⢻⣿⣥⣿⠸⣿⣿⣿⢿⠿⢓⣿⡿⠏⠀⠌⠈\
\n⠶⠶⠾⠛⠛⠉⢉⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⡀⠙⣿⣯⡿⢿⣿⣿⠟⣴⣿⣑⣈⠀⡀⠫⣿⡿⣿⣷⣶⣈\
\n⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⡙⠗⠀⠺⣿⣧⣤⣿⣷⣶⣿⣿⣃⣽⢞⡿⣿⣿⣿⣿⣿⣿⣿⠲⢧⣄⠁\
\n⠀⢀⣀⣤⣤⣤⠄⡀⠀⢀⣀⠀⣀⣀⡠⠤⠔⠐⢺⣽⣿⡶⠀⠀⠀⠉⠙⠉⠉⣯⣆⣿⣿⠁⠠⣘⣭⣿⡿⢿⣿⣿⣿⣿⢧⣦⣗⣌⡀\
\n⣾⣿⡿⠉⠷⣛⣏⡁⠉⠻⣗⣾⣷⣶⣶⣒⣒⣄⣽⣏⣿⣿⣶⣄⠀⠀⢀⠘⣹⢿⣿⣟⢠⣬⣵⣮⣿")
           
#game start
while ready == "Y":
    #R1 
    print("Today is the first day of your new job as a security guard in the office, surrounded by a laptop, cameras and lamps.")
    print("Your job is to fend off the evil cats, and prevent them from getting to you or the office.")
    print("As you settle down, you notice a message from your boss. Will you check it out? (Y/N)")
    choiceR1 = input()
    #R2- bingus and popcat
    if choiceR1 == "N":
        print("Nah, reading messages is for nerds! You close the laptop and notice something.")
        print("Behind the laptop is a TV. On that TV, you recognize the cat. ")
        print("Its Bingus the cat meme, looking very villianous! Do you want to continue to look at him (1) or open the laptop again (2)? Please type 1 or 2:")
        choiceR2 = input()
        #R4 - bingus tv
        if choiceR2 == "1":
            print("You continue to look at Bingus. Wow! What a lovely cat, despite him looking into your soul.")
            print("Suddenly, you feel like its too bright.")
            print("Surely its your lamp! Do you want to switch it off? (Y/N)")
            choiceR4 = input()
            #E1 - bingus good
            if choiceR4 == "Y":
                print("You turn off the lamp. The image of Bingus begins to fade.")
                print("The TV switches to Floppa and below, it reads:'You may have survived this time. Next time, the Evil Bingus will get you!'")
                print("Wow! You dodged a bullet, and luckly survived the night against Bingus. Great job!\n-VANQUISHING BINGUS ENDING-")
                print(bingus)
                break

            #E2 - bingus bad
            if choiceR4 == "N":
                print("You decide not to turn off the lamp. You need to see afterall.")
                print("The TV begins to turn red and glitch and the evil version of Bingus jumps out of the TV.")
                print("The last thing you see is Bignus jumping on to of you. What a tragic fate!\n-MISSION FAILED: PASSING OUT FROM BINGUS ENDING-")
                print(bingus)
                break
            #N/A
            else:
                print("You choice to do nothing! Suddenly, you get sleepy.")
                print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
                print('"Your Bingus!" You say, and the very cat pounces on you.')
                print("-BAD ENDING-\nThe evil Bingus got to you. Please restart program to try again.")
                print(bingus)
                break
                
        #R5 - pop cat laptop
        if choiceR2 == "2":
            print("You decide to open the laptop. Out of sight, out of mind!")
            print("On the laptop, you open camera 2 and see a familiar cat on screen. Its Pop Cat!")
            print("What is Pop Cat doing here? Do you want to continue to look at him (1) or switch cameras (2)? Please type 1 or 2:")
            choiceR5 = input()
            #E3 - pop cat good
            if choiceR5 == "1":
                print("You continue to look at Pop Cat. As time passes, he disappears from the camera.")
                print("As you flick through cameras to find Pop Cat and watch him disappear, the sun begins to rise")
                print("Wow! You have survived the night and fended off Pop Cat. Great job!\n-BEGONE POP CAT ENDING-")
                print()
                break
            #E4 - pop cat bad
            if choiceR5 == "2":
                print("You decide not to look at Pop Cat.")
                print("A few minutes later, you notice something out of the corner of you eye. ")
                print("You lower the laptop screen and get jumpscared by Pop Cat. What an untimely fate!\n-MISSION FAILED: POP CAT JUMPSCARE ENDING-")
                print()
                break
            #N/A
            else:
                print("You choice to do nothing! Suddenly, you get sleepy.")
                print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
                print('"Your Pop Cat!" You say, and the very cat pounces on you.')
                print("-BAD ENDING-\nThe evil Pop Cat got to you. Please restart program to try again.")
                print()
                break
        #N/A    
        else:
            print("You choice to do nothing! Suddenly, you get sleepy.")
            print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
            print('"Your Bingus!" You say, and the very cat pounces on you.')
            print("-BAD ENDING-\nThe evil Bingus got to you. Please restart program to try again.")
            print()
            break

        
    #R3- floppa 
    elif choiceR1 == "Y":
        print('You open the message. In all caps, it reads: "MAKE SURE MY DUMPLLINGS ARE UNTOUCHED."')
        print("How eccentric. Wouldn't they go cold by the time the boss comes back?")
        print("You begin flipping through the cameras to find the room his dumplings are in.")
        print("What camera should you go on? 6 or 8? Please type 6 or 8:")
        choiceR3 = input()
        #R6 floppa door
        if choiceR3 == "6":
            print("You switch to camera 6 and wait a few minutes.")
            print("Suddenly, the lights turn off an you hear knocking at your office door.")
            print("Strange, no one should be here. But seeing takes priority! Do you want to turn the lights back on? (Y/N)")
            choiceR6 = input()
            #E5 - floppa door good
            if choiceR6 == "Y":
                print("You turn the lights back on, and you hear footsteps walking away.")
                print("You wait till your shifts over. Oh no! You forgot to protect the dumplings.")
                print("You send a message to your boss asking for forgiveness, and notice a message.")
                print("Its from Floppa! It read, \"I'll get you next time!\", from Floppa. Yikes, thank goodness you didn't let the evil cat in your office! \n-NO ENTRY FLOPPA! ENDING-")
                print(floppa)
                break
            #E6 - floppa door bad
            if choiceR6 == "N":
                print("You don't turn the lights back on. You don't need the lights that much!")
                print("Footsteps begin to get louder, and you office door opens. ")
                print("However, no one is there? You shift your focus to the laptop, when you get jumpscared by Floppa.")
                print("You let the evil cat into the office! What a tragic fate!\n-MISSION FAILED: FLOPPA ENTRY ENDING-")
                print(floppa)
                break
            #N/A
            else:
                print("You choice to do nothing! Suddenly, you get sleepy.")
                print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
                print('"Your Floppa!" You say, and the very cat pounces on you.')
                print("-BAD ENDING-\nThe evil Floppa got to you. Please restart program to try again.")
                print(floppa)
                break
        #R7 floppa dumplings
        if choiceR3 == "8":
            print("You switch to camera 8 notice something. Its the dumplings your boss wants you to protect!")
            print("Suddenly, the screen flickers and Floppa the evil cat meme is infront of the dumplings.")
            print("He looks so hungry... Do you want to turn a blind eye to him eating your bosses dumplings?(Y/N)")
            choiceR7 = input()
            #E7 - dumplings bad
            if choiceR7 == "Y":
                print("You turn off laptop and wait till your shift ends.")
                print("Your boss enters the building, and its ruined!")
                print("There is a massive mess everywhere, all because you let Floppa eat those dumplings and grow stronger!")
                print("Your boss yells at you for 36 minutes straight, then fires you. Yikes, first day on the job as well!\n-MISSION FAILED: FIRED ENDING-")
                print()
                break
            #E8 - dumplings good
            if choiceR7 == "N":
                print("You stare at Floppa at the screen.")
                print("As if Floppa can feel your stare through the screen, Floppa quickly runs away.")
                print("Throughout the night, you repeat this and defend your bosses dumplings from Floppa.")
                print("When your shift is over, your boss is happy to see his dumplings and you get promoted. Nice, first day on the job as well!\n-PROMOTED ENDING-")
                print()
                break
            #N/A
            else:
                print("You choice to do nothing! Suddenly, you get sleepy.")
                print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
                print('"Your Floppa!" You say, and the very cat pounces on you.')
                print("-BAD ENDING-\nThe evil Floppa got to you. Please restart program to try again.")
                print()
                break
        #N/A
        else:
            print("You choice to do nothing! Suddenly, you get sleepy.")
            print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
            print('"Your Floppa!" You say, and the very cat pounces on you.')
            print("-BAD ENDING-\nThe evil Floppa got to you. Please restart program to try again.")
            print(floppa)
            break
    else:
        print("You choice to do nothing! As you wait, you get sleepy.")
        print("Crash! You hear a noise and wake up to a famous cat meme in you face.")
        print('"Your Floppa!" You say, and the very cat pounces on you.')
        print("-BAD ENDING-\nThe evil Floppa got to you. Please restart program to try again.")
        print(floppa)
        break


#try again
if ready != "Y":
    print("Come back when you are ready. The evil cats will need to be fended off eventually...")  

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
