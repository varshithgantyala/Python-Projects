import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        print("You mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for yes or 'n' for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("No word exists.Try again.")
        else:
            return ("Invalid input. Please enter 'y' or 'n'.")
    else:
        return ("Please enter correct word.")
word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
