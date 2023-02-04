# PROJECT: strong_password_detection.py - A simple program utilising regular
# expressions which determines if a password string passed is strong.

import re

password_input = input("\nEnter password here: ").strip()

# Defining regular expressions for lower/upper case and digits.
lower_case_regex = re.compile(r"[a-z]+")
upper_case_regex = re.compile(r"[A-Z]+")
digit_regex = re.compile(r"\d+")

# Check user input for presence of lower/upper case and digits.
lower_case_detected = lower_case_regex.search(password_input)
upper_case_detected = upper_case_regex.search(password_input)
digit_detected = digit_regex.search(password_input)

# Check if password is at least 8 characters long, has at least 1 upper case,
# lower case and digit.
if len(password_input) < 8:
    print("Password is weak. Must be at least 8 characters long.")
elif None in (lower_case_detected, upper_case_detected, digit_detected):
    print("""Password is weak. Must have at least one lower case, upper case
and digit each""")
else:
    print("Password is strong. Satisfies all requirements.")
