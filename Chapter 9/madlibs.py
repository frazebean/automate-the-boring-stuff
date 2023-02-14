# madlibs.py - A madlibs program.

import re

text_file = open("C:/Users/muadz/Documents/MadLibs.txt")
text_content = text_file.read()

split_text_content = re.findall(r"[\w]+|[.,!?;'()]", text_content)

print(split_text_content)

for index, item in enumerate(split_text_content):
    if "ADJECTIVE" in item:
        adjective_input = input("Enter an adjective: ").strip()
    elif "NOUN" in item:
        noun_input = input("Enter a noun: ").strip()
    elif "ADVERB" in item:
        adverb_input = input("Enter an adverb: ").strip()
    elif "VERB" in item:
        verb_input = input("Enter a verb: ").strip()


