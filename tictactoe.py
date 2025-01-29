def drawBoard(board):
    print("    1   2   3 ")
    print("   ------------")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            print("|", end="")
            print(" " + board[i][j] + " ", end="")
        print("|")

def isValidMove(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ' '

def takeTurn(board, player):
    while True:
        move = input("Enter your move (row, column): (If you want to quit, enter 'E') ").strip().lower()
        if move == "e":
            print("You quit the game!")
            return "bye!"
        else:
            move = move.split(",")
            if len(move) != 2:
                print("Invalid input. Please enter two numbers separated by comma or enter 'E' to quit the game.")
                continue
            row_str, col_str = move
            if not row_str.strip().isdigit() or not col_str.strip().isdigit():
                print("Invalid input. Please enter an integer for row and column.")
                continue
            row = int(row_str)
            col = int(col_str)
            if row not in range(1, 4) or col not in range(1, 4):
                print("The board's size is 3x3. You can enter row and column numbers 1, 2 or 3. Try again:")
                continue
            if not isValidMove(board, row - 1, col - 1):
                print("This place is already taken. Try again:")
                continue
            else:
                board[row - 1][col - 1] = player
                break

def checkWinner(board):
    size = len(board)
    for i in range(size):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return ''

def playGame():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    while True:
        drawBoard(board)
        takeTurn(board, player)
        winner = checkWinner(board)
        if winner:
            drawBoard(board)
            print(f"Congratulations! Player {winner} wins!")
            break
        player = 'O' if player == 'X' else 'X'

playGame()
