# madlibs.py - A madlibs program.

import re

text_file = open("C:/Users/muadz/Documents/Madlibs.txt")
text = text_file.read()

madlibs_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
madlibs_found = madlibs_regex.findall(text)

adjective_input = ''
noun_input = ''
adverb_input = ''
verb_input = ''

for word in madlibs_found:
    if word == "ADJECTIVE":
        adjective_input = input("Enter an adjective: ").strip()
    elif word == "NOUN":
        noun_input = input("Enter a noun: ").strip()
    elif word == "ADVERB":
        adverb_input = input("Enter an adverb: ").strip()
    elif word == "VERB":
        verb_input = input("Enter a verb: ").strip()

modified_text = text.replace("ADJECTIVE", adjective_input)\
    .replace("NOUN", noun_input).replace("ADVERB", adverb_input)\
    .replace("VERB", verb_input)

print(modified_text)
