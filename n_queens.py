def is_safe(board, row, col, n):

    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):

    if col >= n:
        return True

    for row in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter value of N: "))

board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):

    print("\nSolution:")

    for row in board:
        print(row)

else:
    print("No solution exists.")