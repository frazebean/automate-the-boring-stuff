# PROJECT: regex_strip.py - A regex version of Python's strip() function.'

import re

user_input = input("Enter string: ")

# bspace = beginning_space, espace = ending_space
space_regex = re.compile(r"^\s+|\s+$")
space_detected = space_regex.search(user_input)

if space_detected is not None:
    no_space = user_input.replace(space_detected.group(), "")

print(no_space)
