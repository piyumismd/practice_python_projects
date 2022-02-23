
# position define
# (raw, column) --> (1,1) (1,2) (1,3)
#                   (2,1) (2,2) (2,3)
#                   (3,1) (3,2) (3,3)
# player1 -> x
# player2 -> o

def draw_board(board):
    print('   |  |   ')
    print(' ' + board[6] + '  | ' + board[7] + ' | ' + board[8])
    print('   |  |     ')
    print('_______________________')
    print('   |  |     ')
    print(' ' + board[3] + '  | ' + board[4] + ' | ' + board[5])
    print('   |  |     ')
    print('_______________________')
    print(' ' + board[0] + '  | ' + board[1] + ' | ' + board[2])
    print('   |  |     ')


draw_board(['', '', '', '', '', '', '', '', ''])
