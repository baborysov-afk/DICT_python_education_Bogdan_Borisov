import random

LEVELS = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}


def choose_level():
    while True:
        print("Which level do you want? Enter a number:")
        print(f"1 - {LEVELS['1']}")
        print(f"2 - {LEVELS['2']}")
        choice = input().strip()
        if choice in LEVELS:
            return choice
        print("Incorrect format.")


def generate_task(level):
    if level == "1":
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operation = random.choice(["+", "-", "*"])
        if operation == "+":
            answer = a + b
        elif operation == "-":
            answer = a - b
        else:
            answer = a * b
        return f"{a} {operation} {b}", answer

    number = random.randint(11, 29)
    return str(number), number ** 2


def get_user_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def save_result(score, level):
    print("What is your name?")
    name = input().strip()
    entry = f"{name}: {score}/5 in level {level} ({LEVELS[level]}).\n"
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(entry)
    print('The results are saved in "results.txt".')


def main():
    level = choose_level()
    score = 0

    for _ in range(5):
        task, correct_answer = generate_task(level)
        print(task)
        if get_user_answer() == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(
        f"Your mark is {score}/5. "
        "Would you like to save your result to the file? Enter yes or no."
    )
    if input().strip() in ("yes", "YES", "y", "Yes"):
        save_result(score, level)


if __name__ == "__main__":
    main()