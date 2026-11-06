board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

print('Welcome to Tic Tac Toe! Here is the current board:')

turn = 'X'
turns = 0

while turns < 9:
    print(board[0])
    print(board[1])
    print(board[2])

    print(turn + '\'s turn')

    row = int(input('Pick a row: ')) - 1
    column = int(input('Pick a column: ')) - 1

    if row <= len(board) and row > 0 and column <= len(board[row]) and column > 0:
        if board[row][column] == ' ':
            board[row][column] = turn

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            turns += 1
        else:
            print('That space is already taken')
    else:
        print('That space does not exist')
