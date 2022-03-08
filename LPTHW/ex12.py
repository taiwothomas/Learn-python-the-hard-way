from sys import argv
#use argv to get the user's name

script, name, surname = argv

age = input("How old are you? ")
height = input("How tall are you in cm? ")
weight = input("Hoe much do you weigh in kg? ")

print(f"{name} {surname} is {age} years old, {height}cm tall and {weight}kg heavy.")