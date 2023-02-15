# madlibs.py - A madlibs program.

import re

# Open existing 'MadLibs.txt' document to be updated by the player.
text_file = open("C:/Users/muadz/Documents/Madlibs.txt")
text = text_file.read()

# Regular expression for player to replace parts of speech with custom words.
madlibs_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
madlibs_found = madlibs_regex.findall(text)

# Initialise parts of speech input so no error is thrown if a part of speech
# is not present.
adjective_input = ''
noun_input = ''
adverb_input = ''
verb_input = ''

# Parts of speech in text found to be replaced by user input.
for word in madlibs_found:
    if word == "ADJECTIVE":
        adjective_input = input("Enter an adjective: ").strip()
    elif word == "NOUN":
        noun_input = input("Enter a noun: ").strip()
    elif word == "ADVERB":
        adverb_input = input("Enter an adverb: ").strip()
    elif word == "VERB":
        verb_input = input("Enter a verb: ").strip()

# Replace parts of speech with user input.
modified_text = text.replace("ADJECTIVE", adjective_input)\
    .replace("NOUN", noun_input).replace("ADVERB", adverb_input)\
    .replace("VERB", verb_input)

print("")
print(modified_text)

# Create a new text file of the updated mad libs.
new_text_file = open("C:/Users/muadz/Documents/NewMadLibs.txt", 'w')
new_text = new_text_file.write(modified_text)
