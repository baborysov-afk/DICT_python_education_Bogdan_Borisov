import random


def get_initial_pencils():
    """Запитує та перевіряє початкову кількість олівців."""
    while True:
        user_input = input("How many pencils would you like to use:\n> ")

        # Перевірка на числове значення
        if not user_input.isdigit():
            print("The number of pencils should be numeric")
            continue

        pencils = int(user_input)

        # Перевірка на позитивне число
        if pencils == 0:
            print("The number of pencils should be positive")
            continue

        return pencils


def get_first_player(p1, p2):
    """Запитує та перевіряє, хто робить перший хід."""
    while True:
        user_input = input(f"Who will be the first ({p1}, {p2}):\n> ")
        if user_input in [p1, p2]:
            return user_input
        print(f"Choose between '{p1}' and '{p2}'")


def get_bot_move(pencils):
    """Логіка виграшної стратегії для бота (Jack)."""
    # Програшна позиція: n % 4 == 1 (наприклад: 1, 5, 9, 13...)
    if pencils % 4 == 1:
        if pencils == 1:
            return 1
        return random.randint(1, 3)

    # Виграшна позиція: залишити супротивнику кількість олівців, що дорівнює (4k + 1)
    remainder = pencils % 4
    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    elif remainder == 2:
        return 1
    return 1


def get_human_move(pencils):
    """Запитує та перевіряє хід користувача (John)."""
    while True:
        user_input = input("> ")

        # Перевірка: чи введено 1, 2 або 3
        if user_input not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue

        taken = int(user_input)

        # Перевірка: чи не взято більше олівців, ніж є на столі
        if taken > pencils:
            print("Too many pencils were taken")
            continue

        return taken


def main():
    player1 = "John"
    player2 = "Jack"  # Jack — це бот

    # Отримання початкових даних
    pencils = get_initial_pencils()
    current_player = get_first_player(player1, player2)

    # Ігровий цикл
    while pencils > 0:
        print("|" * pencils)

        if current_player == player1:
            print(f"{player1}'s turn!")
            taken = get_human_move(pencils)
        else:
            print(f"{player2}'s turn:")
            taken = get_bot_move(pencils)
            print(taken)

        pencils -= taken

        # Передача ходу наступному гравцеві
        current_player = player2 if current_player == player1 else player1

    # Переможець той, хто НЕ брав останній олівець (тобто той, чия черга зараз)
    print(f"{current_player} won!")


if __name__ == "__main__":
    main()
    