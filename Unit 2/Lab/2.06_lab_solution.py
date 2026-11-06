#Solution for 2.06 Lab - Tic-Tac-Toe Revisited

tic_tac_toe = [1,2,3,4,5,6,7,8,9]
counter = 0
player_x = 0
player_o = 0
x_marker = 'x'
o_marker = 'o'
x_turn = True
o_turn = False
#Game loop
print('Welcome to the game of Tic-Tac-Toe! In this game two players will take turns placing either an x or an o on the gameboard. There are 9 turns in total.')
print(tic_tac_toe[:3])
print(tic_tac_toe[3:6])
print(tic_tac_toe[6:])
while counter < 9:
    while x_turn:
        player_x = int(input('Player X, choose a space to place your marker: '))
        if player_x not in range(1,len(tic_tac_toe)+1):
            print('That space is not on the board')
        elif (tic_tac_toe[player_x - 1] == x_marker) or (tic_tac_toe[player_x - 1] == o_marker):
            print('That space is already filled with a marker, try again.')
        else:
            tic_tac_toe[player_x - 1] = x_marker
            x_turn = False
            o_turn = True
        print(tic_tac_toe[:3])
        print(tic_tac_toe[3:6])
        print(tic_tac_toe[6:])
    while o_turn:
        player_o = int(input('Player O, choose a space to place your marker: '))
        if player_o not in range(1,len(tic_tac_toe)+1):
            print('That space is not on the board')
        elif (tic_tac_toe[player_o - 1] == x_marker) or (tic_tac_toe[player_o - 1] == o_marker):
            print('That space is already filled with a marker, try again.')
        else:
            tic_tac_toe[player_o - 1] = o_marker
            o_turn = False
            x_turn = True
        print(tic_tac_toe[:3])
        print(tic_tac_toe[3:6])
        print(tic_tac_toe[6:])
    counter +=1



    # if player_x not in range(1,10):
        # print('Space number not on board')