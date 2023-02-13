# madlibs.py - A madlibs program.

import re

parts_of_speech = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
parts_of_speech_present = []

text_file = open("C:/Users/muadz/Documents/MadLibs.txt")
text_content = text_file.read()

split_text_content = re.split(r'\W', text_content)

for word in split_text_content:
    if word in parts_of_speech:
        parts_of_speech_present.append(word)

if "ADJECTIVE" in parts_of_speech_present:
    adjective_input = input("Enter an adjective: ").strip()
if "NOUN" in parts_of_speech_present:
    noun_input = input("Enter a noun: ").strip()
if "ADVERB" in parts_of_speech_present:
    adverb_input = input("Enter an adverb: ").strip()
if "VERB" in parts_of_speech_present:
    verb_input = input("Enter a verb: ").strip()
