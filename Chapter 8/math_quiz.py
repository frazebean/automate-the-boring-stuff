# multiplication_quiz.py - A program that asks a number of multiplication
# questions with a timer and allows 3 tries.

import random
import time

number_of_questions = 10  # Number of questions to be given
correct_answers = 0  # Used to display user score at the end of quiz

for question_number in range(number_of_questions):
    tries = 0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    while tries < 3:
        print(f"\n{question_number + 1}) What is {num1} x {num2}?")
        start = time.monotonic()
        response = int(input("Answer: "))
        end = time.monotonic()

        time_elapsed = end - start

        if time_elapsed > 8:
            print("Exceeded 8 second limit. No point awarded.")
            break

        if response == num1 * num2:
            print("Correct!")
            correct_answers += 1
            time.sleep(1)
            break

        elif response != num1 * num2:
            tries += 1
            if tries == 3:
                print("Incorrect. You reached 3 tries. No point awarded.")
                break

            print(f"Incorrect. Try again. You have {3 - tries} tries left.")
            continue
