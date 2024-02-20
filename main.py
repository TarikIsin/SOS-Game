import random
import math
from time import sleep


def initialize_board():
    # 5x5 board with initial "S" symbols on the corners
    board = [['S', ' ', ' ', ' ', 'S'],
             [' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' '],
             ['S', ' ', ' ', ' ', 'S']]
    return board


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def is_valid_move(row, col, current_symbol, selected_symbol, board):
    return 0 <= row < 5 and 0 <= col < 5 and board[row][col] == ' ' and selected_symbol == current_symbol


def is_valid_position(row, col, board_size):
    return 0 <= row < board_size and 0 <= col < board_size


def is_sos(board, row, col, symbol):
    symbol = symbol.upper()
    board_size = len(board)
    counter = 0

    if symbol == "S":
        if (
                is_valid_position(row - 2, col - 2, board_size)
                and board[row - 1][col - 1] == "O"
                and board[row - 2][col - 2] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row - 2, col, board_size)
                and board[row - 1][col] == "O"
                and board[row - 2][col] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row - 2, col + 2, board_size)
                and board[row - 1][col + 1] == "O"
                and board[row - 2][col + 2] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row, col - 2, board_size)
                and board[row][col - 1] == "O"
                and board[row][col - 2] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row, col + 2, board_size)
                and board[row][col + 1] == "O"
                and board[row][col + 2] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 2, col - 2, board_size)
                and board[row + 1][col - 1] == "O"
                and board[row + 2][col - 2] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 2, col, board_size)
                and board[row + 1][col] == "O"
                and board[row + 2][col] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 2, col + 2, board_size)
                and board[row + 1][col + 1] == "O"
                and board[row + 2][col + 2] == "S"
        ):
            counter += 1
    elif symbol == "O":
        if (
                is_valid_position(row - 1, col - 1, board_size)
                and is_valid_position(row + 1, col + 1, board_size)
                and board[row - 1][col - 1] == "S"
                and board[row + 1][col + 1] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row - 1, col, board_size)
                and is_valid_position(row + 1, col, board_size)
                and board[row - 1][col] == "S"
                and board[row + 1][col] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row - 1, col + 1, board_size)
                and is_valid_position(row + 1, col - 1, board_size)
                and board[row - 1][col + 1] == "S"
                and board[row + 1][col - 1] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row, col - 1, board_size)
                and is_valid_position(row, col + 1, board_size)
                and board[row][col - 1] == "S"
                and board[row][col + 1] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row, col + 1, board_size)
                and is_valid_position(row, col - 1, board_size)
                and board[row][col + 1] == "S"
                and board[row][col - 1] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 1, col - 1, board_size)
                and is_valid_position(row - 1, col + 1, board_size)
                and board[row + 1][col - 1] == "S"
                and board[row - 1][col + 1] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 1, col, board_size)
                and is_valid_position(row - 1, col, board_size)
                and board[row + 1][col] == "S"
                and board[row - 1][col] == "S"
        ):
            counter += 1
        if (
                is_valid_position(row + 1, col + 1, board_size)
                and is_valid_position(row - 1, col - 1, board_size)
                and board[row + 1][col + 1] == "S"
                and board[row - 1][col - 1] == "S"
        ):
            counter += 1

    return counter > 0, counter


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game():
    global current_symbol
    print("1 - Human vs Human\n"
          "2 - Human vs AI\n"
          "3 - AI vs AI")
    option = input("What would you like to do: ")
    while option not in ['1', '2', '3']:
        print("Invalid option. Please enter '1' or '2' or '3'.")
        option = input("What would you like to do: ")

    if option == "2":
        board = initialize_board()
        turn = "player"
        player_Point = 0
        ai_Point = 0

        # Moves are taken in turns while the game continues
        while not is_board_full(board):
            print_board(board)

            if "player" in turn:

                current_symbol = input("Enter symbol ('S' or 'O'): ")
                # Continue to ask until the user enters a valid symbol
                while current_symbol not in ['S', 'O', 's', 'o']:
                    print("Invalid symbol. Please enter 'S' or 'O'.")
                    current_symbol = input("Enter symbol ('S' or 'O'): ")

                if current_symbol.upper() == 'O' or current_symbol.upper() == 'S':
                    row = int(input("Enter row (0-4): "))
                    while row not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        row = int(input("Enter row (0-4): "))
                    col = int(input("Enter column (0-4): "))
                    while col not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        col = int(input("Enter column (0-4): "))

                    while not is_valid_move(row, col, current_symbol.upper(), current_symbol.upper(), board):
                        print("Invalid move. Try again.")
                        row = int(input("Enter row (0-4): "))
                        while row not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")
                            row = int(input("Enter row (0-4): "))
                        col = int(input("Enter column (0-4): "))
                        while col not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")
                            col = int(input("Enter column (0-4): "))

                    board[row][col] = current_symbol.upper()

                    check_sos, sos_counter = is_sos(board, row, col, current_symbol)
                    if check_sos:
                        player_Point += sos_counter
                        print("Player created an SOS! Turn skipped.")
                    else:
                        print("Player made a move.")
                turn = "ai"
            else:
                # AI turn
                ai_move, ai_symbol = get_ai_move(board)
                ai_row, ai_col = ai_move
                board[ai_row][ai_col] = ai_symbol
                sleep(1)
                check_sos, sos_counter = is_sos(board, row, col, ai_symbol)
                if check_sos:
                    print("AI created an SOS! Turn skipped.")
                    ai_Point += sos_counter
                else:
                    print("AI made a move.")
                turn = "player"

        print_board(board)
        print("Game over. Final result:")

        print(f"Player Point: {player_Point}!")
        print(f"AI Point: {ai_Point}!")

        if player_Point > ai_Point:
            print("Player wins!")
        elif ai_Point > player_Point:
            print("AI wins!")
        else:
            print("It's a draw!")

    elif option == "1":
        board = initialize_board()
        turn = "player1"
        player1_Point = 0
        player2_Point = 0

        # Moves are taken in turns while the game continues
        while not is_board_full(board):
            print_board(board)

            if "player1" in turn:

                current_symbol = input("Enter symbol ('S' or 'O'): ")
                # Continue to ask until the user enters a valid symbol
                while current_symbol not in ['S', 'O', 's', 'o']:
                    print("Invalid symbol. Please enter 'S' or 'O'.")
                    current_symbol = input("Enter symbol ('S' or 'O'): ")

                if current_symbol.upper() == 'O' or current_symbol.upper() == 'S':
                    row = int(input("Enter row (0-4): "))
                    while row not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        row = int(input("Enter row (0-4): "))
                    col = int(input("Enter column (0-4): "))
                    while col not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        col = int(input("Enter column (0-4): "))

                    while not is_valid_move(row, col, current_symbol.upper(), current_symbol.upper(), board):
                        print("Invalid move. Try again.")
                        row = int(input("Enter row (0-4): "))
                        while row not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")
                            current_symbol = input("Enter symbol ('S' or 'O'): ")
                        col = int(input("Enter column (0-4): "))
                        while col not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")

                    board[row][col] = current_symbol.upper()

                    check_sos, sos_counter = is_sos(board, row, col, current_symbol)
                    if check_sos:
                        player1_Point += sos_counter
                        print("Player 1 created an SOS! Turn skipped.")
                    else:
                        print("Player 1 made a move.")
                turn = "player2"
            else:
                current_symbol = input("Enter symbol ('S' or 'O'): ")
                # Continue to ask until the user enters a valid symbol
                while current_symbol not in ['S', 'O', 's', 'o']:
                    print("Invalid symbol. Please enter 'S' or 'O'.")
                    current_symbol = input("Enter symbol ('S' or 'O'): ")

                if current_symbol.upper() == 'O' or current_symbol.upper() == 'S':
                    row = int(input("Enter row (0-4): "))
                    while row not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        row = int(input("Enter row (0-4): "))
                    col = int(input("Enter column (0-4): "))
                    while col not in [0, 1, 2, 3, 4]:
                        print("Invalid value. Please enter 0, 1, 2, 3, 4")
                        col = int(input("Enter column (0-4): "))

                    while not is_valid_move(row, col, current_symbol.upper(), current_symbol.upper(), board):
                        print("Invalid move. Try again.")
                        row = int(input("Enter row (0-4): "))
                        while row not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")
                            row = int(input("Enter row (0-4): "))
                        col = int(input("Enter column (0-4): "))
                        while col not in [0, 1, 2, 3, 4]:
                            print("Invalid value. Please enter 0, 1, 2, 3, 4")
                            col = int(input("Enter column (0-4): "))

                    board[row][col] = current_symbol.upper()

                    check_sos, sos_counter = is_sos(board, row, col, current_symbol)
                    if check_sos:
                        player2_Point += sos_counter
                        print("Player 2 created an SOS! Turn skipped.")
                    else:
                        print("Player 2 made a move.")
                turn = "player1"

        print_board(board)
        print("Game over. Final result:")

        print(f"Player 1 Point: {player1_Point}!")
        print(f"Player 2 Point: {player2_Point}!")

        if player1_Point > player2_Point:
            print("Player 1 wins!")
        elif player2_Point > player1_Point:
            print("Player 2 wins!")
        else:
            print("It's a draw!")

    elif option == '3':
        board = initialize_board()
        turn = "ai1"
        ai1_Point = 0
        ai2_Point = 0

        # Moves are taken in turns while the game continues
        while not is_board_full(board):
            print_board(board)

            if "ai1" in turn:
                # AI1 turn
                ai_move, ai_symbol = get_ai_move(board)
                ai_row, ai_col = ai_move
                board[ai_row][ai_col] = ai_symbol
                sleep(1)

                check_sos, sos_counter = is_sos(board, ai_row, ai_col, ai_symbol)
                if check_sos:
                    ai1_Point += sos_counter
                    print("AI 1 created an SOS! Turn skipped.")
                else:
                    print("AI 1 made a move.")
                turn = "ai2"
            else:
                # AI2 turn
                ai_move, ai_symbol = get_ai_move2(board)
                ai_row, ai_col = ai_move
                board[ai_row][ai_col] = ai_symbol
                sleep(1)
                check_sos, sos_counter = is_sos(board, ai_row, ai_col, ai_symbol)
                if check_sos:
                    ai2_Point += sos_counter
                    print("AI 2 created an SOS! Turn skipped.")
                else:
                    print("AI 2 made a move.")
                turn = "ai1"

        print_board(board)
        print("Game over. Final result:")

        print(f"AI 1 Point: {ai1_Point}!")
        print(f"AI 2 Point: {ai2_Point}!")

        if ai1_Point > ai2_Point:
            print("AI 1 wins!")
        elif ai2_Point > ai1_Point:
            print("AI 2 wins!")
        else:
            print("It's a draw!")


def get_ai_move(board):
    symbols = ['S', 'O']
    symbol = random.choice(symbols)

    # Check each empty position on the board
    empty_positions = [(i, j) for i in range(5) for j in range(5) if board[i][j] == ' ']

    for position in empty_positions:
        row, col = position

        symbol2 = random.choice(symbols)
        board[row][col] = symbol2
        check_sos, sos_count = is_sos(board, row, col, symbol2)
        if check_sos:
            # If SOS is formed, return the move and the symbol
            return position, symbol2
        undo_move(board, row, col)  # Undo move

        symbol3 = random.choice(symbols)
        while symbol3 == symbol2:
            symbol3 = random.choice(symbols)
        board[row][col] = symbol3
        check_sos, sos_count = is_sos(board, row, col, symbol3)
        if check_sos:
            # If SOS is formed, return the move and the symbol
            return position, symbol3
        undo_move(board, row, col)  # Undo move

    # If no SOS move is found, choose a strategic move
    random.shuffle(empty_positions)
    for position in empty_positions:
        row, col = position

        # Check if placing 'S' will not create an SOS opportunity for the opponent
        for i in range(2):
            symbol4 = random.choice(symbols)
            if symbol4 == 'S':
                symbol5 = 'O'
            else:
                symbol5 = 'S'

            if i == 1:
                board[row][col] = symbol4
                if not is_sos_opportunity(board, symbol5):
                    return position, symbol4
                undo_move(board, row, col)  # Undo move
            else:
                board[row][col] = symbol5
                if not is_sos_opportunity(board, symbol4):
                    return position, symbol5
                undo_move(board, row, col)  # Undo move

    move = random.choice(empty_positions)
    ai_row, ai_col = move
    board[ai_row][ai_col] = symbol

    # If no strategic move is found, choose a random empty position
    return move, symbol


def is_sos_opportunity(board, opponent_symbol):
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                board[i][j] = opponent_symbol
                check_sos, sos_count = is_sos(board, i, j, opponent_symbol)
                if check_sos:
                    undo_move(board, i, j)  # Undo move
                    return True
                board[i][j] = ' '  # Undo the move
    return False


def get_ai_move2(board):
    symbols = ['S', 'O']
    symbol = random.choice(symbols)

    # Check each empty position on the board
    empty_positions = [(i, j) for i in range(5) for j in range(5) if board[i][j] == ' ']

    for position in empty_positions:
        row, col = position

        # Try placing 'S'
        board[row][col] = 'S'
        check_sos, sos_count = is_sos(board, row, col, 'S')
        if check_sos:
            # If SOS is formed, return the move and the symbol
            return position, 'S'
        board[row][col] = ' '  # Undo the move

        # Try placing 'O'
        board[row][col] = 'O'
        check_sos, sos_count = is_sos(board, row, col, 'O')
        if check_sos:
            # If SOS is formed, return the move and the symbol
            return position, 'O'
        board[row][col] = ' '  # Undo the move

    # If no SOS move is found, choose a random empty position
    return random.choice(empty_positions), symbol


def minimax(board, depth, maximizing_player, alpha, beta, symbol):

    if maximizing_player:
        max_eval = -math.inf
        for i in range(5):
            for j in range(5):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    evaluate = minimax(board, depth - 1, False, alpha, beta, symbol)
                    undo_move(board, i, j)  # Undo move
                    max_eval = max(max_eval, evaluate)
                    alpha = max(alpha, evaluate)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(5):
            for j in range(5):
                if board[i][j] == ' ':
                    board[i][j] = 'S' if symbol == 'O' else 'O'
                    evaluate = minimax(board, depth - 1, True, alpha, beta, symbol)
                    undo_move(board, i, j) # Undo move
                    min_eval = min(min_eval, evaluate)
                    beta = min(beta, evaluate)
                    if beta <= alpha:
                        break
        return min_eval


def undo_move(board, row, col):
    board[row][col] = ' '


if __name__ == "__main__":
    play_game()
