
# possible winnings
# matrix [0][0] = [1][0] = [2][0] - column
# matrix [0][1] = [1][1] = [2][1]
# matrix [0][2] = [1][2] = [2][2]
# matrix [0][0] = [0][1] = [0][2] i = i for i in matrix [0] - row
# matrix [1][0] = [1][1] = [1][2] i = i for i in matrix [1]
# matrix [2][0] = [2][1] = [2][2] i = i for i in matrix [2]
# matrix [0][0] = [1][1] = [2][2] - diagonal
# matrix [0][2] = [1][1] = [2][0]

def line_match(matrix):
    # rows
    for i in range(0, 3):
        row = [matrix[i][0], matrix[i][1], matrix[i][2]]
        row = set(row)
        if len(row) == 1 and matrix[i][0] != 0:
            return matrix[0][i]

    # columns
    for i in range(0, 3):
        column = [matrix[0][i], matrix[1][i], matrix[2][i]]
        column = set(column)
        if len(column) == 1 and matrix[0][i] != 0:
            return matrix[i][0]

    # diagonals
    diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diag2 = [matrix[0][2], matrix[1][1], matrix[2][1]]

    if len(diag1) == 1 or len(diag2) == 1 and matrix[1][1] != 0:
        return matrix[1][1]

    return 0


winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


print(line_match(no_winner))
