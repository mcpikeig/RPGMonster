from random import randint
import json

#Import JSON Monster Data
with open(r"C:\Users\mcpik\Desktop\Visual Studio Practice\Py Projects\MonsterData.JSON", 'r') as jsonMonster: 
        monster = json.load(jsonMonster)

#Import JSON Modifier Data
with open(r"C:\Users\mcpik\Desktop\Visual Studio Practice\Py Projects\ModifierData.JSON", 'r') as jsonMods: 
        mods = json.load(jsonMods)

#Repeats if user specifies "yes" at end
repeat = True
while repeat:
    
    #Randomizes i to generate a random monster from the list
    length = len(monster["Monsters"]) - 1
    i = randint(0, length)

    #Randomizes HP and Armor values (+-25% HP and +-1 Armor)
    hpdiff = randint(int(monster["Monsters"][i]["HP"]*0.25*-1), int(monster["Monsters"][i]["HP"]*0.25))
    armdiff = randint(-1,1)

    #Rolls to see if you get a special monster (25% Chance) and applies modifiers to stats and prints special monster
    specchance = randint(0,3)
    if specchance == 1:
        modlength = len(mods["Modifiers"]) - 1
        modchance = randint(0,modlength)
        print(mods["Modifiers"][modchance]["Name"],monster["Monsters"][i]["Name"],'\n',"Hit Points:",monster["Monsters"][i]["HP"] + hpdiff,'\n',"Armor:",monster["Monsters"][i]["Armor"] + armdiff,'\n',"Strength:",monster["Monsters"][i]["Strength"] + mods["Modifiers"][modchance]["StrMod"],'\n',"Intelligence:",monster["Monsters"][i]["Intelligence"] + mods["Modifiers"][modchance]["IntMod"],'\n',"Agility",monster["Monsters"][i]["Agility"] + mods["Modifiers"][modchance]["AgMod"],'\n')
        print("Another Monster?")
        repeat = ("y" or "yes") in input().lower()

#Lists the normal monster Stats
    else:
        print(monster["Monsters"][i]["Name"],'\n',"Hit Points:",monster["Monsters"][i]["HP"] + hpdiff,'\n',"Armor:",monster["Monsters"][i]["Armor"] + armdiff,'\n',"Strength:",monster["Monsters"][i]["Strength"],'\n',"Intelligence:",monster["Monsters"][i]["Intelligence"],'\n',"Agility",monster["Monsters"][i]["Agility"],'\n')
        print("Another Monster?")
        repeat = ("y" or "yes") in input().lower()