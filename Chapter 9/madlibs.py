# madlibs.py - A madlibs program.

import re

text_file = open("C:/Users/muadz/Documents/MadLibs.txt")
text_content = text_file.read()

split_text_content = re.findall(r"[\w]+|[.,!?;'()]", text_content)
modified_text_content = []

print(split_text_content)

for index, item in enumerate(split_text_content):
    if "ADJECTIVE" in item:
        adjective_input = input("Enter an adjective: ").strip()
        modified_text_content.append(adjective_input)
    elif "NOUN" in item:
        noun_input = input("Enter a noun: ").strip()
        modified_text_content.append(noun_input)
    elif "ADVERB" in item:
        adverb_input = input("Enter an adverb: ").strip()
        modified_text_content.append(adverb_input)
    elif "VERB" in item:
        verb_input = input("Enter a verb: ").strip()
        modified_text_content.append(verb_input)
    else:
        modified_text_content.append(item)
