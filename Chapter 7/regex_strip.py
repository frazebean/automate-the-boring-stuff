# PROJECT: regex_strip.py - A regex version of Python's strip() function.'

import re

user_input = input("Enter string: ")

# Create a regex that finds trailing beginning and ending spaces.
space_regex = re.compile(r"^\s+|\s+$")
space_detected = space_regex.search(user_input)

# Any trailing space detected will be replaced with "" (no space).
if space_detected is not None:
    no_space = user_input.replace(space_detected.group(), "")

print(no_space)
