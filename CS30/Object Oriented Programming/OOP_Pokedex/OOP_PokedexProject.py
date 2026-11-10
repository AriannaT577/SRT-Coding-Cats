#task 1 code should go here

#-----------panda imports/dataframe stuff------------
#https://pandas.pydata.org/docs/user_guide/10min.html# <--- link for my future reference 
#%pip install pandas
import pandas as pd
df1 = pd.read_csv("Object Oriented Programming/OOP_Pokedex/ndex_names_AT.csv") #assign national pokedex names to the dataframe
df2 = pd.read_csv("Object Oriented Programming/OOP_Pokedex/pokemon_data_type_AT.csv") #assign pokemon data (type and species) to the dataframe
df3 = pd.read_csv("Object Oriented Programming/OOP_Pokedex/pokedex_flavour_AT.csv") #assign pokemon data (flavour text) to the dataframe
#print(df1) #prints entire dataframe (df) of pokedex

df1Subset = df1[["ndex_id", "name_english", "identifier"]] #gets important labels
df2Subset = df2[["Type 1","Type 2", "Classification_info"]] 
df3Subset = df3[["info"]] 

dataFrame = pd.concat([df1Subset, df2Subset, df3Subset], axis=1) #merge the dataframes together
#print(dataFrame) #prints only ndexdi, name_eng, identifier, type, species, and the info description

#-----------classes code section (may get larger?)------------
class pokemon: #parent class?
    def __init__(self, ndexId, nameEng, type1, type2, species, info):
        self.ndexId = ndexId
        self.nameEng = nameEng
        self.type1 = type1
        self.type2 = type2
        self.species = species
        self.info = info
    def __str__(self):
        return f"#{self.ndexId:04d}: {self.nameEng}" #returns id (in three digits, like 001 or 100) and name
        
    def describe(self):
        if self.type2 != "" and str(self.type2) != "nan": 
            #if there are two types -> empty cell **need to use str otherwise will print as fire and nan type
            combinedType = f"{self.type1} and {self.type2}"
        else:
            combinedType = f"{self.type1}"
            
        return ( #multiple lines so its easier to read
        f"\nPokédex Entry #{self.ndexId:04d}: {self.nameEng}, " #national dex id and name
        f"the {self.species} Pokemon. It is a {combinedType}-type Pokemon. \n{self.info}" #typing and species
    )

#-----------automatic indexing------------
pokeDex = [] #list?

for index, row in dataFrame.iterrows(): #interrows() iterates over the rows as (index, series) 
    cID, cName, cIdentifier, cType1, cType2, cSpecies, cInfo = row[[ #assign each row t
        "ndex_id", "name_english", "identifier","Type 1", "Type 2","Classification_info", "info"]] 
    try:
        newPoke = pokemon(cID,cName,cType1,cType2,
                          cSpecies,cInfo) #creates class object with varibale name of pokemon, split into two lines for readability
        pokeDex.append(newPoke)
        exec(f"{cIdentifier} = newPoke") #cIdentifier didnt work as a class?
        #exec(f'print({currentIdentifier})') #prints __str__
        #exec(f'print({cIdentifier}.describe())') #prints description
    except ValueError:
        continue
#print(eevee)

#----------------interface----------------
while True:
    print("\n- Welcome to the Pokedex look up. Type q to quit. -")
    poke = input("What Pokemon would you like to look up? Please type in their name or dex number.\n ")
    poke = poke.lower() #converts to lowercase
    
    if poke == "q": #if you type in q
        print("Goodbye!")
        break #exit loop

    if poke.isdigit(): #if a digit/dex number was typed in
        pID = int(poke) #user input is converted from string to integer
        try:
            searchPoke = pokeDex[pID - 1] #remove one, as index starts at 0, and looks up the __ entry in list, aka dex
            print(searchPoke.describe())
        except (IndexError, TypeError): #if it was a typo or a number greater then 1025
            print(f"Dex number '{poke}' was not found. Please try a valid number, or type in the Pokemon's Name.")
            
    else:
        try:
            exec(f"print({poke}.describe())")
        except NameError: #if there was a typo
            print(f"'{poke}' was not found. Please check your spelling, or type in the Dex number.")
        
#CODE TO REMOVE/NOT NEEDED/EXTRA MESSING AROUND
#-----------panda test------------
dex = dataFrame.loc[:,["ndex_id"]]
name = dataFrame.loc[:,["name_english"]]
identifier = dataFrame.loc[:,["identifier"]]

leafeon_df = dataFrame["name_english"]== "Leafeon" #in the row name_english, true/false statement if its named leafeon

leafeonRow1 = dataFrame.loc[leafeon_df] #checks database for which ROW makes above statement true
#print(leafeonRow1) #prints row (index and names in all languages)

leafeonRow2 = dataFrame.loc[leafeon_df, ["ndex_id", "name_english"]] #searches only within national index and the english name
#print(leafeonRow2) #prints row (index and english name only)
