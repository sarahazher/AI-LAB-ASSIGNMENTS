def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    def solve(board, row):
        if row == n:
            solutions.append(["".join("Q" if col == 1 else "." for col in row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(row)
        print()

n = 4  # Change n to the desired board size
solutions = solve_n_queens(n)
print(f"Found {len(solutions)} solutions for {n}-Queens:")
print_solutions(solutions)
