import tkinter as tk
from tkinter import simpledialog
import os
import json
import random
from tkinter.constants import CENTER, NW, SW

os.chdir(r'YOUR_OS_PATH_HERE')

root = tk.Tk()

frame = tk.Frame(root, bg="cyan")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def getPass():
    place = simpledialog.askstring("Input", "What Company/App/account/website's password would you like to retrieve?\nEnter the name of the Company/App/Website/Account.",
                                   parent=root)
    with open('passwords.json','r') as json_file:
        data = json.load(json_file)
    
    for x in data:
        if x['PlaceName'] == place:
            label = tk.Label(frame, text=f"{x['PlaceName']} : {x['Password']}", bg="gray")
            label.pack()

def genPass():
    #GETTING ALL INPUTS FOR GENERATION
    word1Set = simpledialog.askstring("Input", "Please input one random word.",
                                   parent=root)
    word2Set = simpledialog.askstring("Input", "Please input one random word.",
                                   parent=root)
    word3Set = simpledialog.askstring("Input", "Please input one random word.",
                                   parent=root)
    word4Set = simpledialog.askstring("Input", "Please input one random word.",
                                   parent=root)
    place = simpledialog.askstring("Input", "For which website/app/account/company are you making this password?\nType the website/app/account/company name to save the password with the name.")
    #GETTING A RANDOM LETTER FROM EACH WORD HERE
    letter1 = set(word1Set).pop()
    letter2 = set(word2Set).pop()
    letter3 = set(word3Set).pop()
    letter4 = set(word4Set).pop()

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

    label = tk.Label(frame, text=f"Final Password for {place} : {finalPassword}", bg="gray")
    label.pack()


getPassButton = tk.Button(root, text="Get Passwords", padx=10, pady=5, fg="cyan", bg="#263D42", command=getPass)
getPassButton.pack()

genPassButton = tk.Button(root, text="Generate a Password", padx=10, pady=5, fg="cyan", bg="#263D42", command=genPass)
genPassButton.pack()

root.mainloop()
