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
