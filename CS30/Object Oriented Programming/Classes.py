#-----------class-----------
class Student:
    def __init__(self, name, age, favPokemon, favClass): #predefined characteristics
        self.name = name
        self.age = age #integer
        self.favPokemon = favPokemon
        self.favClass = favClass
    def __str__(self): #predefined string
        return (f"My name is {self.name}, and I am {self.age} years old. My favourite Pokémon is {self.favPokemon}, and my favourite class in school is {self.favClass}.")
        
#    def greeting (self): #predefined dialouge no1
#        print(f"Hello. My name is {self.name}. It's nice to meet you!")

#-----------task 1: students-----------
students=[ #list of 5 predefined students
    Student("Arianna", 16, "Eevee", "Math"),
    Student("Eliana", 16, "Diglett", "Chemistry"),
    Student("Caitlin", 16, "Wigglytuff", "Chemistry"),
    Student("Kabir", 16, "Charizard", "Social Studies"),
    Student("Dan", 34, "Flareon", "Physics")
]
for student in students:
    #print (students) #prints location
    print(student) #prints __str__ for each student

#-----------challenge: inputting students-----------
students_list=[]
while True:
    repeat = input("Would you like in add a student? Please type y/n")
    if repeat != "y":
        print("Okay, bye!")
        break
    name = input ("Please type in the student's name:")
    age = int(input("Please type in the student's age: (This must be an INTEGER/NUMBER)"))
    favPokemon = input ("Please type in the student's favorite Pokémon:")
    favClass = input ("Please type in the student's favorite class:") 
    
    new_student = Student(name, age, favPokemon, favClass) #creates student based on class attributes
    students_list.append(new_student) #adds new inputted student into list
    
for student in students_list:
    #print (students) #prints location
    print(student) #prints __str__ for each student