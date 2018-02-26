count = int(input(""))
stringResult = []


for mainIterate in range(count):

    number = int(input(""))
    zeroMatrix = [[0 for col in range(number)] for row in range(number)]
    countQueen = 0
    rowCountQueen = 0
    colCountQueen = 0

    tempRowCountQueen = rowCountQueen
    for rowIterate in range(number):

        tempColCountQueen = colCountQueen
        for colIterate in range(number):

            if zeroMatrix[[rowIterate], [colIterate]] == 0:
                zeroMatrix[[rowIterate], [colIterate]] = 2

                createColOneMatrix(zeroMatrix, rowIterate, colIterate)
                createDiaOneMatrix(zeroMatrix, rowIterate, colIterate)
                colCountQueen += 1

                colIterate=range(number)


        if colIterate == range(number):
            if tempColCountQueen == colCountQueen:
                rowIterate = range(number)
            else : countQueen += colCountQueen







def findZeroCell(matrix, row, col):




def createRowOneMatrix(matrix, row, col):
    for iterate in range(matrix[:1]):
        if row-iterate>=0: matrix[[row-iterate],[col]] = 1
        if row+iterate<=range(matrix[:1]): matrix[[row+iterate],[col]] = 1

    if row == range(matrix[:0]):
        return matrix
    else :
        for subIterate in range(row, range(matrix[:0])):


def createColOneMatrix(matrix, row, col):
    for iterate in range(matrix[1:]):
        if col+iterate<=range(matrix[:1]): matrix[[row],[col+iterate]] = 1

    return matrix


def createDiaOneMatrix(matrix, row, col):
    for iterate in range(matrix[1:]):
        if row+iterate<-range(matrix[:1]) || col+iterate<=range(matrix[1:]): matrix[[row+iterate],[col+iterate]] = 1
        if row+iterate<=range(matrix[:1]) || col-iterate>=0: matrix[[row+iterate],[col-iterate]] = 1

    return matrix


def ifPlaceQueen(matrix, row, col):
    if matrix[[row],[col]] == 0:
        return True
    else :
        return False


def recursiveQueen(matrix, n) :
    if n == 0:
        return matrix


    for col in range(number):
        matrix[[row], [col]] == 1 #퀸 두기

        if ifPlaceQueen(matrix, row, col) == False:
            row += 1
            rowFlag = True

        if rowFlag == True:
            col += 1
        else:
            col -= 1

    if row == number:
        return 1:
    else :

        recursiveQueen()
        return :










for iterate in range(len(stringResult)):
    print(stringResult[iterate])

