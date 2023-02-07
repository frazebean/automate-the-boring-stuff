# multiplication_quiz.py - A program that asks a number of multiplication
# questions with a timer and allows 3 tries.

import random
import time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    tries = 0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    while tries < 3:
        print(f"\nWhat is {num1} x {num2}?")
        response = int(input("Answer: "))

        if response == num1 * num2:
            print("Correct!")
            correct_answers += 1
            time.sleep(1)
            break

        elif response != num1 * num2:
            print(f"Incorrect. Try again. You have {3 - tries} tries.")
            tries += 1
            continue
