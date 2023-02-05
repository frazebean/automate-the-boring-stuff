# PROJECT: regex_strip.py - A function made with Python's regular expressions
# that acts similar to the in-built 'strip()' function.

import re

# This regex removes whitespaces from the beginning and end of the string, if
# no arguments are passed.
wspace_regex = re.compile(r"^\s+|\s+$")  # 'wspace' stands for 'whitespace'
wspace_detected = wspace_regex.findall("")
print(wspace_detected)

# This regex removes any character in a string when the character is specified
# in the function's second argument.
character_regex = re.compile(r"\S+")
character_detected = character_regex.findall("")
print(character_detected)
