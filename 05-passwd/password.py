# Password Generator project by Robert Laurie
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
qty_letters = int(input("How many letters would you like in your password?\n"))
qty_symbols = int(input(f"How many symbols would you like?\n"))
qty_numbers = int(input(f"How many numbers would you like?\n"))
chars = []
chars.extend(random.choices(letters, k=qty_letters))

chars.extend(random.choices(symbols, k=qty_symbols))
chars.extend(random.choices(numbers, k=qty_numbers))
random.shuffle(chars)
password = ''.join(chars) # Convert list of characters to string
print(f"Your new password is:\n{password}")