import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word was not found."

q = "y"
while q == "y":
    
    w = input("Enter Word: ")   
    print(translate(w))
    q = input("To use the dictionary again press 'y' else press 'n'.")
    if q == "n":
        print("Thank you")


    
    
