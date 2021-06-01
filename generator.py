import random

word1Set = set(input("Name any random word (1/4).\n"))
word2Set = set(input("Name any random word (2/4).\n"))
word3Set = set(input("Name any random word (3/4).\n"))
word4Set = set(input("Name any random word (4/4).\n"))

letter1 = word1Set.pop()
letter2 = word2Set.pop()
letter3 = word3Set.pop()
letter4 = word4Set.pop()

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
number3 = random.randint(1, 10)
number4 = random.randint(1, 10)
number5 = random.randint(1, 10)

finalPassword = f"{number1}{letter1}{number2}{letter2}{number3}{letter3}{number4}{letter4}{number5}"
print(f"Here is your final password - {finalPassword}")