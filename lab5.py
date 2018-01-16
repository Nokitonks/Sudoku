#Stefan Orton-Urbina
#sortonur
#15-122 Section B
#September 26th, 2017
import string
import math
import cs112_f17_week5_linter

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

def testAdjacentSpace():

    print("testing...")
    assert((adjacentSpace([[1,2,3], [4,5,6], [7,8,9]], 1) == True))
    assert((adjacentSpace([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == False))
    print("passed!")

def testisKingsTour():
    board1 = [[1,2,3],[6,5,4],[7,8,9]]
    board2 =  [
        [  1, 14, 15, 16],
        [ 13,  2,  8,  6],
        [ 12,  8,  3,  5],
        [ 11, 10,  9,  4]
    ]

    print("testing...King")
    assert(isKingsTour(board1) == True)
    assert(isKingsTour(board2) == False)
    assert(isKingsTour([[3, 2, 1], [6, 4, 9], [5, 7, 8]]) == True)
    assert(isKingsTour([[3, 2, 9], [6, 4, 1], [5, 7, 8]]) == False)
    print("passed..Yeet")

def testIsLegalSudoku():
    print("THIS IS THE BIG ONE")

    board = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
    board1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 6, 0, 8, 0, 0, 7, 9]
    ]
    assert(isLegalSudoku(board) == True)
    assert(isLegalSudoku(board1) == False)

    print("Very NICE!")

def testAreLegalValues():
    print("Testing LegalValues stuff")
    assert(areLegalValues([1,2,3,4,5,6,0,7,7]) == False)
    assert (areLegalValues([1, 2, 3, 4, 5, 6, 0, 7]) == False)
    assert (areLegalValues([1, 2, 3, 4, 0, 0, 0, 7, 8]) == True)
    print("nice legal thingy is working")

def testAll():
    testAdjacentSpace()
    testisKingsTour()
    testAreLegalValues()
    testIsLegalSudoku()

def main():
    cs112_f17_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()