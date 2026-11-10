#%pip install matplotlib #needed to run this graph
import matplotlib.pyplot as plt #this is a graphing function module, very useful for data visualization in Python
import random as r #allows for random lists, using r instead of random bc its shorter
'''
you can use the following code to help store your values (the idx variable will return the position of the Type string in that array. 
For example, the sample code looks for the str "Water" and returns an answer of 9, the string at position 9 in the array.
'''
typeCount = [0 for i in range(16)] #Makes an array of 16 entries, each with a value of 0. KEEP THIS OUTSIDE OF YOUR LOOP
typeArray = ["Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", 
                 "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark"] 
#-------------------------------------my code-------------------------------------------
class HiddenPower():
    def __str__(self):
        return f"This pokemon has a {self.HPType}-type Hidden Power move."
        
    #[HP, Atk, Def, Speed, SpAtk, SpDef] aka order of ivs
    def __init__(self, iv):
        self.iv=iv
        self.calculateType()
    def calculateType (self):
        bitList = [] #stores them in list so i dont overwrite them later
        for iv in self.iv: #covert each iv (repeats 5 times) to bit/odd/even
        #-----------binary-----------
#            binary = format(iv, '05b') #referenced stackoverflow pls dont ai flag me
#            bit = int(binary[-1]) #grabs least significant bit aka rightmost, [-1] is like the last index
#            bitList.append(bit)
        #------------odd/even?----------
            if iv % 2 == 0: #no remainder is even
                bitList.append(0) #adds 0, as if least significant digit is 0
            else: #off, aka has a reminder
                bitList.append(1)
            
        a, b, c, d, e, f = bitList #assigns each bit from binary iv to a variable
        typeIndex =  int(((a + 2*b + 4*c + 8*d + 16*e + 32*f) * 15)/63) #funky math written above
        #self.HPType = self.typeArray[typeIndex] #stores hidden power from its corresponding type index
        self.HPType = typeArray[typeIndex] #MAKE SURE ITS PUBLIC*********

#------------------------------------------my code for lists/random--------------------------------------
trials = 10000
for i in range(trials): #aka for each of the 10000 trials
    iv = [r.randint(0, 31) for i in range(6)] #generates random list of 6 numbers
    yourFlareon = HiddenPower(iv)
    idx = typeArray.index(yourFlareon.HPType) #this code should pull the string for your Flareon's HP type and tell you 
                                            #which position in the typeArray corresponds to that type. 
    typeCount[idx] += 1
    #idx = typeArray.index("Water") #example code, yours should be calling the attribute HPType in your class object. Use this to keep track of which 
                                   #trait has just been calculated!

#Keep this code as-is. 
print(typeCount)
probabilityArray = [i/100 for i in typeCount] #You can make an array as a for loop in this way. Very handy trick to shorten the lines of 
                                              #code you need, but if it is more confusing to you, there's nothing wrong with using a regular
                                              #loop and the .append() function! Just a slightly more elegant method.
print(probabilityArray)
