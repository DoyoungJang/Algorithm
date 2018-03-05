global number
routineCounter = int(input(""))
K = 0
stringResult = []

def printSolution(board):
    global K
    K = K+1


def isSafe(board, row, col):

    # check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    #  check upper side of col
    for i in range(col):
        if board[i][col] == 1:
            return False

    # check diagonal of left upper side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    # check diagonal of left lower side
    for i,j in zip(range(row,number,1), range(col,-1,-1)):   #row에서 N까지 1씩, col에서 -1까지 -1씩.
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col >= number:
        printSolution(board);
        return True

    for i in range(number): #모든 행을 하나하나 순회.
        if isSafe(board, i, col):
            board[i][col] = 1

            solveNQUtil(board, col+1)

            board[i][col] = 0

    return False

def solveNQ():
    board = [[0 for col in range(number)] for row in range(number)]
    Counter = 0


    if solveNQUtil(board, 0) == False:
        return False
    else :
        Counter += 1


    printSolution(board)

    return True

if routineCounter > 0:
    if routineCounter <= 12:
        for i in range(routineCounter):
            number = int(input(""))
            K = 0
            solveNQ()
            stringResult.append(K)

for iterate in range(len(stringResult)):
    print(stringResult[iterate])