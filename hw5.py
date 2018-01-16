import cs112_f17_week5_linter
from tkinter import *
from Python.week5.sudoku import *
import copy

#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################


#Draws our sudoku board
def drawBoard(canvas, data):

    margin = 10
    boxWidth = (data.width-margin*2)/9
    hLight = "ivory2"
    letterColor = "black"
    data.gameOver = 1

    #Goes through every square and fills it in with the correct graphics
    for row in range(9):
        for col in range(9):
            #Makes sure the game isnt over yet
            if data.board[row][col] == 0:
                data.gameOver = 0

            #Makes the light colored squares (81 of them)
            if(data.highlightRow == row) and (data.highlightCol == col):
                hLight = "firebrick1"
            canvas.create_rectangle(margin+row*boxWidth,margin+col*boxWidth\
            ,margin+row*boxWidth+boxWidth,\
            margin+col*boxWidth+boxWidth, fill = hLight)
            hLight = "ivory2"

            #Creates the number in the boxes
            #(If number is user inputed, makes it blue)
            if (data.board[row][col] != 0):
                if (data.board[row][col] != data.startBoard[row][col]):
                    letterColor = "blue2"
                canvas.create_text(margin+row*boxWidth+boxWidth/2,\
                margin+col*boxWidth+boxWidth/2, fill = letterColor,\
                text = str(data.board[row][col]),font = ("Helvetica","25"))
            letterColor = "black"

    #Creates the thick borders between boxes
    boxWidth = (data.width-margin*2)/3
    for row in range(3):
        for col in range(3):
            canvas.create_rectangle(margin+row*boxWidth,margin+col*boxWidth\
                                    ,margin+row*boxWidth+boxWidth,\
                                    margin+col*boxWidth+boxWidth, width = 6)

    #Makes data.gameOver 1 and creates the end screen
    if data.gameOver == 1:
        canvas.create_rectangle(0,data.height*3/8,data.width,data.height*5/8,\
                                fill = "magenta3")
        canvas.create_text(data.width/2,data.height/2,\
                           font = ("Helvetica", "30"), fill = "black",\
                           text = "Great job!! You're a winner :)!")


def init(data):
    # Creates all the necessary data
    data.gameOver = 0
    data.startBoard = copy.deepcopy(data.board)
    highlightRow = 4
    highlightCol = 4
    data.highlightRow = highlightRow
    data.highlightCol = highlightCol
    pass

def keyPressed(event, data):

    #User cant input if game is over
    if data.gameOver == 1:
        return None

    #Makes sure number inputed is legal and not in an already input space
    if event.keysym.isdigit() and event.keysym != "0":
        if data.board[data.highlightRow][data.highlightCol] == 0:
            data.board[data.highlightRow][data.highlightCol] = int(event.keysym)
            if not isLegalSudoku(data.board):
                data.board[data.highlightRow][data.highlightCol] = 0
    #Only deletes if the number is user inputed
    if event.keysym == "BackSpace":
        if data.startBoard[data.highlightRow][data.highlightCol] == 0:
            data.board[data.highlightRow][data.highlightCol] = 0

    #Moves around the highlight box
    #each has an wrap around case to account for edge wrap arounds
    if event.keysym == "Right":
        if data.highlightRow == 8:
            data.highlightRow = 0
        else:
            data.highlightRow += 1
    if event.keysym == "Left":
        if data.highlightRow == 0:
            data.highlightRow = 8
        else:
            data.highlightRow -= 1
    if event.keysym == "Up":
        if data.highlightCol == 0:
            data.highlightCol = 8
        else:
            data.highlightCol -= 1
    if event.keysym == "Down":
        if data.highlightCol == 8:
            data.highlightCol = 0
        else:
            data.highlightCol += 1
    pass

def redrawAll(canvas, data):
    # draw in canvas
    drawBoard(canvas, data)
    pass

def playSudoku(sudokuBoard, width=500, height=500):
    #Makes sure everything updates and redraws correctly

    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    #If a key is pressed redraw everything
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    board = [
[1,2,3,4,5,6,7,8,9],
[5,0,8,1,3,9,6,2,4],
[4,9,6,8,7,2,1,5,3],
[9,5,2,3,8,1,4,6,7],
[6,4,1,2,9,7,8,3,5],
[3,8,7,5,6,4,0,9,1],
[7,1,9,6,2,3,5,4,8],
[8,6,4,9,1,5,3,7,2],
[2,3,5,7,4,8,9,1,6]
]
    playSudoku(board)

if __name__ == '__main__':
    main()
