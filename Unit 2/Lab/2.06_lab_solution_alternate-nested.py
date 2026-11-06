board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

print('Welcome to Tic Tac Toe! Here is the current board:')

game = True
turn = 'X'

while game:
    print(board[0])
    print(board[1])
    print(board[2])

    print(turn + '\'s turn')

    row = int(input('Pick a row: ')) - 1
    column = int(input('Pick a column: ')) - 1

    if row <= len(board) and column <= len(board[row]):
        if board[row][column] == ' ':
            board[row][column] = turn

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print('That space is already taken')
    else:
        print('That space does not exist')
