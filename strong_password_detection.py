# PROJECT: strong_password_detection.py - A simple program utilising regular
# expressions which determines if a password string passed is strong.

# AUTHOR: Muadz Shakir

import re

password_strength_regex = re.compile(r"[a-zA-Z.\d]{8,}")
password_detected = password_strength_regex.search("aaaaaaaa")
print(password_detected)

print("hello")
