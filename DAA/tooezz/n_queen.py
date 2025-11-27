# 8 Queens using Backtracking
def solve_queens(board, row):
    if row == 8:                        # all queens placed
        return True

    for col in range(8):
        if is_safe(board, row, col):    # check where queen can be placed
            board[row][col] = 1
            if solve_queens(board, row+1):
                return True
            board[row][col] = 0         # backtrack

    return False


def is_safe(board, row, col):
    for i in range(row):                # check column
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:            # left diagonal
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    i, j = row, col
    while i >= 0 and j < 8:             # right diagonal
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    return True


board = [[0]*8 for _ in range(8)]
solve_queens(board, 0)
for row in board:
    print(row)
