# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

import random

password = ""
for n in range(0, nr_letters):
    # rnd_num = random.randint(0, len(letters) - 1)
    # selected_letter = letters[rnd_num]
    #               or
    # selected_letter = random.choice(letters)
    # password += selected_letter
    #               or
    password += random.choice(letters)

print(password)

for n in range(0, nr_symbols):
    # rnd_num = random.randint(0, len(symbols) - 1)
    # selected_symbol = symbols[rnd_num]
    #                 or
    # selected_symbol = random.choice(symbols)
    # password += selected_symbol
    #                 or
    password += random.choice(symbols)

print(password)

for n in range(0, nr_numbers):
    # rnd_num = random.randint(0, len(numbers) - 1)
    # selected_number = numbers[rnd_num]
    #                 or
    # selected_number = random.choice(numbers)
    # password += selected_number
    #                 or
    password += random.choice(numbers)

print(password)
