#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner. Returns True if a player has won."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    """Returns True if the board has no empty spaces left."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """Prompts the user until they enter a valid integer between 0 and 2."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid row and column
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # Check if the current player won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()

