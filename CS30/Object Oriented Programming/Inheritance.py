#-----------Classes (npc and prof)-----------
class npc: #parent class
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.talkCount = 0 #challenge: talk to npc multiple times with different dialouge
    def greeting (self):
        self.talkCount+=1 #adds to counter
        if self.talkCount == 1: #first time interacting
            return f"{self.name}: Hello there fellow Pokemon Trainer! Welcome to Iki Town."
        elif self.talkCount == 2:
            return f"{self.name}: Back again? Nice day for walking around, isn't it?"
        else:
            return f"{self.name}: I'm a bit busy right now, but make sure to talk to Kahuna Hala for your starter Pokemon!"

class professor (npc): #child class
    def __init__(self, name, starters): #inherits from npc
        super().__init__(name, role="professor") #kahuna hala aka pokemon sun/moon
        self.starters = starters
    def greeting(self):
        self.talkCount += 1
        if self.talkCount == 1:
            return f"{self.name}: Welcome to Iki Town! Ready to pick your starter Pokemon?"
        elif self.talkCount == 2:
            return f"{self.name}: Ah, welcome back! Have you looked at the starter Pokemon options yet?"
        else: #any number over 3
            return f"{self.name}: Still deciding? Rowlet, Litten, and Popplio are all waiting for you!"
    def openStarters(self): #special page for picking your starter
        return f"\n--- Choose your starter! ---\n1. Rowlet - Grass Type\n2. Litten - Fire Type\n3. Popplio - Water Type\n"
        
trainer = npc("Youngster", "Trainer", )
prof = professor("Kahuna Hala", "Village Kahuna")

# ----------- Main Yip Yap Loop-----------
print("Welcome to the Iki Town!\n")

while True:
    print("Who would you like to speak to?")
    print("[A] Speak to Youngster (Trainer)\n[B] Speak to Kahuna Hala (Village Kahuna)\n[Q] Quit ")
    choice1 = input("\nChoose an option: ")

    if choice1 == "A": #generic npc
        print("\n" + trainer.greeting() + "\n")
        
    elif choice1 == "B": #prof npc
        print("\n" + prof.greeting())
        print("  [1] Greet again") #
        print("  [2] Choose your starter Pokemon:")
        choice2 = input("Choose option: ")
        if choice2 == "2":
            print(prof.openStarters())
        else:
            print()

    elif choice1 == "Q":
        print("Thanks for playing!")
        break
        
    else:
        print("Please try again. (Make sure to capitalize your letters!) \n")