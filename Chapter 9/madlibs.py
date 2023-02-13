# madlibs.py - A madlibs program.

import re

text_file = open("C:/Users/muadz/Documents/MadLibs.txt")
text_content = text_file.read()
modified_text = []

for word in re.split(r"\W", text_content):
    if "ADJECTIVE" in word:
        adjective_input = input("Enter an adjective: ").strip()
        modified_text.append(adjective_input)
    elif "NOUN" in word:
        noun_input = input("Enter a noun: ").strip()
        modified_text.append(noun_input)
    elif "ADVERB" in word:
        adverb_input = input("Enter an adverb: ").strip()
        modified_text.append(adverb_input)
    elif "VERB" in word:
        verb_input = input("Enter a verb: ").strip()
        modified_text.append(verb_input)
    else:
        modified_text.append(word)

print(modified_text)
