#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

### Your lab5 functions below ###

#Simply tests if n is a perfect square
def isSquare(n):

    if n**.5 == int(n**.5):
        return True
    return False

#returns true if a number n is surrounded on any side by n+1
def adjacentSpace(board, n):
    locNRow = 0
    locNCol = 0
    locN1Row = 0
    locN1Col = 0

    #goes through every space
    for row in range(len(board)):
        for col in range(len(board[row])):

            #finds n and n+1
            if board[row][col] == n:
                locNRow = row
                locNCol = col
            elif board[row][col] == n + 1:
                locN1Row = row
                locN1Col = col
    #Tests if they are adjacent by checking that the diff in both x and y is <=1
    if abs(locNRow-locN1Row)<=1 and abs(locNCol-locN1Col)<= 1:
        return True
    else:
        return False

#Returns true if the board is a KingsTour
def isKingsTour(board):

    #determines the max number that can be in board is
    #returns false if a not allowed number is in board
    numBoard = len(board) ** 2
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]< 1 or board[row][col] > numBoard :
                return False

    #returns false if number in board occurs more than once
    checkingList = ""
    for row in range(len(board)):
        for col in range(len(board[row])):
            #essentially creates a list of numbers and makes sure each one
            #occurs no more than once
            checkingList += str(board[row][col])
            if checkingList.count(str(board[row][col])) > 1:
                return False

    #Checks if each number is adjacent to the # following it
    for i in range(1, numBoard):
        if not adjacentSpace(board, i):
            return False
    else:return True

#Deteremines if a list of numbers are legal for scrabble rules
def areLegalValues(value):

    #make sure its a perfect square length
    if not isSquare(len(value)):
        return False

    #Makes sure that no number but 0 occurs more than once
    #And that no number outside the range exsists
    for i in range(len(value)):
        if len(value) - i < 0:
            return False
    for i in range(len(value)):
        j = value[i]
        if j != 0 and value.count(j) > 1:
            return False
    return True

#Finds the row and sends it to areLegalValues
def isLegalRow(board, row):

    if areLegalValues(board[row]):
        return True
    return False

#Finds cols and sends it to areLegalValues
def isLegalCol(board, col):

    workingCol = []
    for row in board:
        workingCol.extend([row[col]])

    if areLegalValues(workingCol):
        return True
    return False

#Finds blocks and sends to areLegalValues
def isLegalBlock(board, block):

    workingBlock = []
    lenBlock = int(len(board)**.5)
    startRow = (block//lenBlock)*lenBlock
    startCol = (block%lenBlock)*lenBlock

    for row in range(startRow,startRow+lenBlock):
        for col in range(startCol, startCol + lenBlock):
            workingBlock.extend([board[row][col]])


    if areLegalValues(workingBlock):
        return True
    return False

#Uses all the helper fuctions above to check every aspect of the board
def isLegalSudoku(board):

    for i in range(len(board)):
        if not isLegalRow(board, i):
            return False
        if not isLegalCol(board, i):
            return False
        if not isLegalBlock(board, i):
            return False
    return True