board = [" " for i in range(9)]


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner():
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for line in lines:
        a, b, c = line
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None



def minimax(is_maximizing):
    res = winner()
    if res == "O":  
        return 1
    if res == "X":  
        return -1
    if " " not in board:  
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def get_ai_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


print("TIC TAC TOE")
print("1. Human vs Human")
print("2. Human vs AI")

# Mode Selection
while True:
    mode = input("Select Game Mode (1 or 2): ").strip()
    if mode in ["1", "2"]:
        break
    print("Invalid choice! Please enter 1 or 2.")

current_player = "X"

while True:
    show_board()

    
    if mode == "2" and current_player == "O":
        print("AI is making a move...")
        pos = get_ai_move()
    else:
        
        try:
            pos = (
                int(input(f"Player {current_player}, enter position (1-9): "))
                - 1
            )
        except ValueError:
            print("Please enter a valid number!")
            continue

        
        if pos < 0 or pos > 8:
            print("Invalid position! Please choose a number between 1 and 9.")
            continue

        
        if board[pos] != " ":
            print("Position already taken!")
            continue

   
    board[pos] = current_player

    
    if winner():
        show_board()
        if mode == "2" and current_player == "O":
            print("AI wins!")
        else:
            print(f"Player {current_player} wins!")
        break

  
    if " " not in board:
        show_board()
        print("It's a draw!")
        break

   
    current_player = "O" if current_player == "X" else "X"

