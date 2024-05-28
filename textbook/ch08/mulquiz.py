import random
import time

def math_quiz(number_of_questions=10):
    correct_answers = 0

    for question_number in range(number_of_questions):
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
        answer = num1 * num2
        prompt = f'#{question_number + 1}: {num1} x {num2} = '

        attempts = 0
        while attempts < 3:
            user_input = input(prompt)
            if not user_input.isdigit():
                print('Invalid input. Please enter a number.')
                continue

            user_answer = int(user_input)
            if user_answer == answer:
                print('Correct!')
                correct_answers += 1
                break
            else:
                print('Incorrect!')
                attempts += 1
                if attempts == 3:
                    print('Out of tries!')
                time.sleep(1)

    print(f'Score: {correct_answers} / {number_of_questions}')

math_quiz()
