import json

filename = 'starting_with_python/userName.json'
# filename = "C:/Users/Sergio/Desktop/ejercicios_python/starting_with_python/userName.json" 
name = ''

try:
    with open(filename, 'r') as r:
        name = json.load(r)
except:
    print("First time login")

if name != "":
    print("Welcome back, " + name["name"] + "!")
else:
    name = input("Hello! What's your name? ")
    print("Welcome " + name + "!")
