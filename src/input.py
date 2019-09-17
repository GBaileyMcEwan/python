#!/usr/bin/python3

name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"Your name was {name} and your age was {age}.")
print(f"Your age divided by 2 is: {age / 2}")
if name == "Gorgs":
    print("You're such a nerd")
elif name == "Diego":
    print("Would you like some Ciabatta?")
else:
    print("I don't know you!")
