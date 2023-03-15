import random

num_of_questions = 5
score = 0

for i in range(num_of_questions):
    a = random.randint(10, 90)
    b = random.randint(1, 9)

    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        result = a + b
        question = f"{a} + {b} = ?"
    elif operator == '-':
        a, b = max(a, b), min(a, b)
        result = a - b
        question = f"{a} - {b} = ?"
    elif operator == '*':
        a = random.randint(1, 9)
        result = a * b
        question = f"{a} * {b} = ?"
    else:
        result = a // b
        a = result * b
        question = f"{a} / {b} = ?"

    print(f"Питання {i + 1}: {question}")
    try:
        c = int(input())
    except ValueError:
        print("Неправильний ввід. Будь ласка, введіть число.")
        continue

    if result == c:
        score += 1
        print(f"Вірно! Ваш рахунок {score}")
    else:
        print(f"Неправильно. Відповідь: {result}. Ваш рахунок {score}")

print(f"Ваш остаточний рахунок {score}/{num_of_questions}")
