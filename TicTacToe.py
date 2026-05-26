import math

# Create board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # cols
        [0,4,8], [2,4,6]             # diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9) : ")) - 1

            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")

        except:
            print("Please enter a number between 1 and 9.")

# Main game loop
def play_game():

    print(" ------- Welcome to Tic-Tac-Toe AI -------- \n")
    print("You are X and AI is O")

    print_board()

    while True:

        # Player turn
        player_move()
        print_board()

        if check_winner("X"):
            print("Congratulations! You Won!")
            break

        if is_draw():
            print("It's a Draw!")
            break

        # AI turn
        print("AI is making a move....")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI Wins!")
            break

        if is_draw():
            print("It's a Draw!")
            break

# Run game
play_game()