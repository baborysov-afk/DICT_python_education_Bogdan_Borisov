def print_board(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


def check_state(board):
    # Отримуємо всі рядки, стовпчики та діагоналі
    lines = []

    # Рядки
    lines.extend(board)

    # Стовпчики
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # Діагоналі
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    x_wins = ['X', 'X', 'X'] in lines
    o_wins = ['O', 'O', 'O'] in lines

    # Підрахунок символів
    all_cells = [cell for row in board for cell in row]
    x_count = all_cells.count('X')
    o_count = all_cells.count('O')
    has_empty = ' ' in all_cells or '_' in all_cells

    if (x_wins and o_wins) or abs(x_count - o_count) >= 2:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif not has_empty:
        return "Draw"
    else:
        return "Game not finished"


def main():
    # Початкова порожня дошка (3х3 з пробілами)
    board = [[' ' for _ in range(3)] for _ in range(3)]

    current_player = 'X'
    print_board(board)

    while True:
        coordinates = input("Enter the coordinates: ").split()

        # Перевірка на введення чисел
        if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("You should enter numbers!")
            continue

        row = int(coordinates[0]) - 1
        col = int(coordinates[1]) - 1

        # Перевірка меж (координати від 1 до 3)
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates should be from 1 to 3!")
            continue

        # Перевірка на зайнятість комірки
        if board[row][col] != ' ' and board[row][col] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        # Встановлюємо хід
        board[row][col] = current_player
        print_board(board)

        # Перевірка стану гри після ходу
        state = check_state(board)
        if state in ["X wins", "O wins", "Draw"]:
            print(state)
            break

        # Зміна черги гравця
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
