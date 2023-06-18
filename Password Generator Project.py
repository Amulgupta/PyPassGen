#Password Generator Project

import random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


option = int(input(("Choose 1 for generating an easy password and 2 for generating a hard password: ")))


if option == 1:
  #Easy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  password = ""
  for char in range(1, nr_letters + 1):
    password += random.choice(letters)

  for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

  print(f"You chose option 1.\nSo your password order will not be randomized and will be in the following order of letters then symbols and then numbers.\nYour generated password is: {password}")


elif option == 2:
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  password_list = []
  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  # print(password_list)

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(
      symbols)  # Appending a list and this is the same thing.

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  # print(password_list)
  password = ""
  random.shuffle(password_list)

  for char in password_list:
    password += char

  print(f"You chose option 2.\nSo your password will be in a randomised order of letters, numbers and symbols which makes it nearly impossible and unguessable.\nYour generated password is {password}")


else:
  print("Sorry! You chose an invalid option.")
