board = [" "] * 9

def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def game_over(board):
    return " " not in board or any(board[i] == board[i + 1] == board[i + 2] != " " for i in range(0, 9, 3)) or any(board[i] == board[i + 3] == board[i + 6] != " " for i in range(3)) or (board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ")

def evaluate(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == "X":
            return 1
        elif board[condition[0]] == board[condition[1]] == board[condition[2]] == "O":
            return -1
    return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    if depth == 0 or game_over(board):
        return evaluate(board)

    max_eval = -float("inf") if is_maximizing else float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X" if is_maximizing else "O"
            eval = minimax(board, depth - 1, not is_maximizing, alpha, beta)
            board[i] = " "
            max_eval = max(max_eval, eval) if is_maximizing else min(max_eval, eval)
            alpha = max(alpha, eval) if is_maximizing else alpha
            beta = min(beta, eval) if not is_maximizing else beta
            if beta <= alpha:
                break
    return max_eval

def best_move(board):
    best_eval, best_move, alpha, beta = -float("inf"), -1, -float("inf"), float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 3, False, alpha, beta)
            board[i] = " "
            if eval > best_eval:
                best_eval, best_move = eval, i
    return best_move

while not game_over(board):
    display_board(board)
    user_move = int(input("Enter your move (0-8): "))
    if board[user_move] == " ":
        board[user_move] = "O"
    else:
        print("Invalid move. Try again.")
        continue

    if not game_over(board):
        ai_move = best_move(board)
        board[ai_move] = "X"

display_board(board)
result = evaluate(board)
if result == 1:
    print("You win!")
elif result == -1:
    print("AI wins!")
else:
    print("It's a tie!")
# This code implements a simple game of Tic-Tac-Toe where a player competes against an AI opponent. 
# The game uses the minimax algorithm to determine the AI's moves and evaluate the game state. Here's how the code works:

# board: This list represents the Tic-Tac-Toe board with 9 cells, initially filled with empty strings.

# display_board(board): This function displays the current state of the Tic-Tac-Toe board, dividing it 
# into rows and columns. It prints the board to the console.

# game_over(board): This function checks if the game is over. It returns True if any of the following conditions are met:

# The board is full (no empty cells remain).
# Any row, column, or diagonal has the same symbol (either "X" or "O").
# evaluate(board): This function evaluates the current state of the board and returns:

# 1 if "X" wins (the AI).
# -1 if "O" wins (the player).
# 0 for a tie.
# minimax(board, depth, is_maximizing, alpha, beta): This is the minimax algorithm implementation 
# with alpha-beta pruning.

# depth is the current depth in the game tree.
# is_maximizing is a boolean flag that indicates if it's the AI's turn.
# alpha and beta are used for alpha-beta pruning.
# The algorithm explores all possible moves at each step and evaluates the game state recursively. 
# It returns the best possible evaluation for the AI or player. Alpha-beta pruning is used to eliminate 
# unnecessary exploration of branches when it's clear that they won't lead to better outcomes.

# best_move(board): This function finds the best move for the AI by evaluating all possible moves and 
# selecting the one with the highest minimax value. It calls the minimax function for each possible move 
# and returns the best move's index.

# The main loop:

# The game continues as long as game_over(board) returns False, indicating that the game is not over.
# The current state of the board is displayed.
# The player is prompted to enter their move (an integer from 0 to 8) where they want to place 
# "O" (the player's symbol).
# If the selected cell is empty, "O" is placed in that cell. If not, an error message is displayed, and the player is prompted to try again.
# If the game is still not over, the AI makes its move ("X") by calling best_move(board) and 
# updating the board with the chosen move.
# After the game ends, the final state of the board is displayed.

# The result variable is assigned the evaluation of the board using the evaluate function.

# The program prints the outcome of the game based on the result. If it's 1, the player wins. If it's -1, 
# the AI wins. If it's 0, it's a tie.

# This code allows a player to play against an AI opponent in a game of Tic-Tac-Toe and uses the minimax algorithm
#  to make intelligent decisions for the AI's moves.