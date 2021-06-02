import random
import os
import json

os.chdir(r'C:\Users\arjun\Documents\Arjun\coding\python\passwordGen')

userChoice = input("Hey there! Welcome to CPG.\nWhat would you like to do? Type\u001b[1m\u001b[31m password \u001b[0m for a list of your passwords.\nType\u001b[1m\u001b[31m generate\u001b[0m for generating a new password.\n")

if userChoice == 'password':
    place = input('Please input the EXACT name of website / account / app name you had saved your password with. \u001b[1m\u001b[31mCase sensitive is true.\u001b[0m \n')
    with open('passwords.json','r') as json_file:
        data = json.load(json_file)
    
    for x in data:
        if x['PlaceName'] == place:
            print(x['PlaceName'] + ' : ' + x['Password'])
elif userChoice == 'generate':
    #INPUTTING EVERYTHING
    word1Set = set(input("Name any random word (1/4).\n"))
    word2Set = set(input("Name any random word (2/4).\n"))
    word3Set = set(input("Name any random word (3/4).\n"))
    word4Set = set(input("Name any random word (4/4).\n"))
    place = input("For which website are you making this password?\nType the website/app/account name.\n")

    #GETTING A RANDOM LETTER FROM EACH WORD HERE
    letter1 = word1Set.pop()
    letter2 = word2Set.pop()
    letter3 = word3Set.pop()
    letter4 = word4Set.pop()

    #GENERATING THE RANDOM NUMBERS HERE
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 10)
    number4 = random.randint(1, 10)
    number5 = random.randint(1, 10)

    #GETTING THE FINAL PASSWORD, DUMPING/APPENDING NEW PASS AND PRINTING IT.
    finalPassword = f"{number1}{letter1}{number2}{letter2}{number3}{letter3}{number4}{letter4}{number5}"

    with open("passwords.json") as json_file:
        data = json.load(json_file)
    
        newPass = {
            "PlaceName":place,
            "Password":finalPassword
        }

        data.append(newPass)

    with open('passwords.json','w') as f:
        json.dump(data, f,indent=4)

    print(f"Here is your final password - {finalPassword}")
else:
    print("Not an option.")