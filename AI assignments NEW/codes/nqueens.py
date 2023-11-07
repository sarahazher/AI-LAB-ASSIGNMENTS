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
# This code is an implementation of the N-Queens problem, a classic combinatorial problem where the goal is to
# place N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens 
# should share the same row, column, or diagonal. Here's an explanation of how the code works:

# 1. `is_safe` Function:
#    - The `is_safe` function checks if it is safe to place a queen in a given position on the chessboard. 
# It takes four parameters: `board`, `row`, `col`, and `n`.
#    - It first checks if there is a queen in the same column by examining the elements in the column 
# for all rows up to the current row.
#    - Next, it checks the upper-left diagonal for any queens that might threaten the current position.
#    - Finally, it checks the upper-right diagonal for any threatening queens.
#    - If no queens are found in any of the checked directions, the function returns `True`, indicating that
# it is safe to place a queen in the given position.

# 2. `solve_n_queens` Function:
#    - The `solve_n_queens` function is the main function for solving the N-Queens problem.
#    - It defines a nested function named `solve` that recursively explores the solutions. 
# This function is responsible for finding all possible solutions.
#    - It initializes an empty list called `solutions` to store the found solutions.
#    - It creates a 2D `board` (a list of lists) of size `n x n`, initially filled with zeros to represent the chessboard.

# 3. `solve` Function:
#    - The `solve` function uses a backtracking approach to find all solutions to the N-Queens problem.
#    - If it reaches the `row == n` condition, it means that a solution has been found, so it appends 
# a textual representation of the solution to the `solutions` list. The textual representation consists 
# of strings where "Q" represents a queen and "." represents an empty space.
#    - The function recursively explores all possible queen placements, trying every column for the 
# current row. If a safe placement is found, it proceeds to the next row.
#    - After the recursive exploration, it resets the current position on the `board` to 0 
# (indicating no queen), allowing further exploration.

# 4. `print_solutions` Function:
#    - The `print_solutions` function is responsible for displaying the found solutions.
#    - It iterates through the list of solutions and prints each solution's chessboard representation.

# 5. Setting the `n` Value and Finding Solutions:
#    - You can change the value of `n` to determine the size of the chessboard and the number of 
# queens to be placed. For example, in the provided code, `n` is set to 4.
#    - The code then calls the `solve_n_queens` function with the specified `n` to find all possible solutions.

# 6. Displaying Solutions:
#    - After finding solutions, the code prints the number of solutions found and then calls the 
# `print_solutions` function to display each solution's chessboard representation.

# The code demonstrates a Python implementation of solving the N-Queens problem using a recursive
# backtracking algorithm. It finds and displays 
# all valid solutions for the given chessboard size (`n`).