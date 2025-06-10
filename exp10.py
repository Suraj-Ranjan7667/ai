N = 8

def printSolution(board):
    for row in board:
        print(' '.join(map(str, row)))

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] or \
           (row - i >= 0 and board[row - i][col - i]) or \
           (row + i < N and board[row + i][col - i]):
            return False
    return True

def solveNQUtil(board, col):
    if col == N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solveNQ():
    board = [[0]*N for _ in range(N)]
    if not solveNQUtil(board, 0):
        print("No solution")
        return False
    printSolution(board)
    return True

solveNQ()
