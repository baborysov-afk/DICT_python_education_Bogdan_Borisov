def parse_number(token: str):
    return float(token) if "." in token else int(token)


def read_matrix(size_prompt: str, matrix_prompt: str):
    rows, cols = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = [
        [parse_number(x) for x in input().split()]
        for _ in range(rows)
    ]
    return rows, cols, matrix


def print_matrix(matrix, round_digits=None):
    print("The result is:")
    for row in matrix:
        formatted = []
        for val in row:
            if round_digits is not None:
                val = round(val, round_digits)
                if val == 0:
                    val = 0
            formatted.append(str(val))
        print(" ".join(formatted))


def add_matrices(r1, c1, m1, r2, c2, m2):
    if r1 != r2 or c1 != c2:
        return None
    return [
        [m1[i][j] + m2[i][j] for j in range(c1)]
        for i in range(r1)
    ]


def multiply_by_constant(rows, cols, matrix, const):
    return [
        [matrix[i][j] * const for j in range(cols)]
        for i in range(rows)
    ]


def multiply_matrices(r1, c1, m1, r2, c2, m2):
    if c1 != r2:
        return None
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def transpose_matrix(rows, cols, matrix, mode: str):
    if mode == "1":
        return [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    elif mode == "2":
        return [
            [matrix[rows - 1 - j][cols - 1 - i] for j in range(rows)]
            for i in range(cols)
        ]
    elif mode == "3":
        return [row[::-1] for row in matrix]
    elif mode == "4":
        return matrix[::-1]
    return None


def get_minor(matrix, row_to_remove: int, col_to_remove: int):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col_to_remove]
        for i in range(len(matrix))
        if i != row_to_remove
    ]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sign = (-1) ** col
        minor = get_minor(matrix, 0, col)
        det += sign * matrix[0][col] * determinant(minor)
    return det


def inverse_matrix(rows, cols, matrix):
    if rows != cols:
        return "ERROR_SIZE"

    det = determinant(matrix)
    if det == 0:
        return "NO_INVERSE"

    if rows == 1:
        return [[1 / matrix[0][0]]]

    cofactors = []
    for i in range(rows):
        cofactor_row = []
        for j in range(cols):
            minor = get_minor(matrix, i, j)
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * determinant(minor))
        cofactors.append(cofactor_row)

    adjugate = transpose_matrix(rows, cols, cofactors, "1")
    return [
        [adjugate[i][j] / det for j in range(cols)]
        for i in range(rows)
    ]


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            r1, c1, m1 = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
            r2, c2, m2 = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
            res = add_matrices(r1, c1, m1, r2, c2, m2)
            print_matrix(res) if res is not None else print("The operation cannot be performed.")
        elif choice == "2":
            r, c, m = read_matrix("Enter size of matrix: ", "Enter matrix:")
            const = parse_number(input("Enter constant: ").strip())
            print_matrix(multiply_by_constant(r, c, m, const))
        elif choice == "3":
            r1, c1, m1 = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
            r2, c2, m2 = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
            res = multiply_matrices(r1, c1, m1, r2, c2, m2)
            print_matrix(res) if res is not None else print("The operation cannot be performed.")
        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            t_choice = input("Your choice: ").strip()
            r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")
            res = transpose_matrix(r, c, m, t_choice)
            print_matrix(res) if res is not None else print("The operation cannot be performed.")
        elif choice == "5":
            r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")
            if r != c:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print(determinant(m))
        elif choice == "6":
            r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")
            res = inverse_matrix(r, c, m)
            if res == "ERROR_SIZE":
                print("The operation cannot be performed.")
            elif res == "NO_INVERSE":
                print("This matrix doesn't have an inverse.")
            else:
                print_matrix(res, round_digits=2)


if __name__ == "__main__":
    main()