# Basic AI for graphical Tic Tac Toe game

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

def init(data):
    data.mode = "splashScreen"
    data.turn = "X"
    data.XSlots = []
    data.OSlots = []
    data.oneone = "empty"
    data.onetwo = "empty"
    data.onethree = "empty"
    data.twoone = "empty"
    data.twotwo = "empty"
    data.twothree = "empty"
    data.threeone = "empty"
    data.threetwo = "empty"
    data.threethree = "empty"
    data.XPatterns = ""
    data.OPatterns = ""
    data.gameOver = "False"
    data.counter = 0
    data.show = "normal"

####################################
# Mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"):
        splashScreenMousePressed(event, data)
    elif (data.mode == "instructions"):
        instructionsMousePressed(event, data)
    elif (data.mode == "playGame"):
        playGameMousePressed(event, data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "instructions"): instructionsRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)


################################
# Splash screen
################################

def splashScreenMousePressed(event, data):
    if 230 < event.x < 370 and 475 < event.y < 505:
        data.mode = "instructions"
    if 220 < event.x < 380 and 380 < event.y < 420:
        data.mode = "playGame"

def splashScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="Welcome to Tic-Tac-Toe!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2,
                       text="A simple AI demonstration by Alex Sahinidis",
                       font="Arial 11 bold")
    canvas.create_text(data.width/2, 400,
                       text="PLAY GAME", font="Arial 24 bold")
    canvas.create_text(data.width/2, 490,
                       text="INSTRUCTIONS", font="Arial 16 bold")
    canvas.create_rectangle(220, 380, 380, 420, outline="black")
    canvas.create_rectangle(230, 475, 370, 505, outline="black")

################################
# Instructions screen
################################

def instructionsMousePressed(event, data):
    if 230 < event.x < 370 and 475 < event.y < 505:
        data.mode = "splashScreen"

def instructionsRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-20,
                       text="Instructions", font="Arial 26 bold")
    canvas.create_text(data.width/2, 490,
                       text="HOME SCREEN", font="Arial 16 bold")
    canvas.create_rectangle(230, 475, 370, 505, outline="black")

################################
# Play mode
################################

def playGameMousePressed(event, data):
    if 230 < event.x < 370 and 535 < event.y < 565:
        init(data)
    if data.gameOver != "False" and (230 < event.x < 370 and 350 < event.y < 390):
        data.show = "hidden"


    # Move Locations
    elif data.turn == "X":
        if 92 < event.x < 213 and 92 < event.y < 213 and data.oneone == "empty":
            data.XSlots.append((100, 100, 205, 205))
            data.XSlots.append((205, 100, 100, 205))
            data.turn = "O"
            data.oneone = "occupied"
            data.XPatterns += "1"
            data.counter += 1
        elif 237 < event.x < 358 and 92 < event.y < 213 and data.onetwo == "empty":
            data.XSlots.append((245, 100, 350, 205))
            data.XSlots.append((350, 100, 245, 205))
            data.turn = "O"
            data.onetwo = "occupied"
            data.XPatterns += "2"
            data.counter += 1
        elif 382 < event.x < 508 and 92 < event.y < 213 and data.onethree == "empty":
            data.XSlots.append((390, 100, 495, 205))
            data.XSlots.append((495, 100, 390, 205))
            data.turn = "O"
            data.onethree = "occupied"
            data.XPatterns += "3"
            data.counter += 1
        elif 92 < event.x < 213 and 237 < event.y < 358 and data.twoone == "empty":
            data.XSlots.append((100, 245, 205, 350))
            data.XSlots.append((205, 245, 100, 350))
            data.turn = "O"
            data.twoone = "occupied"
            data.XPatterns += "4"
            data.counter += 1
        elif 237 < event.x < 358 and 237 < event.y < 358 and data.twotwo == "empty":
            data.XSlots.append((245, 245, 350, 350))
            data.XSlots.append((350, 245, 245, 350))
            data.turn = "O"
            data.twotwo = "occupied"
            data.XPatterns += "5"
            data.counter += 1
        elif 382 < event.x < 508 and 237 < event.y < 358 and data.twothree == "empty":
            data.XSlots.append((390, 245, 495, 350))
            data.XSlots.append((495, 245, 390, 350))
            data.turn = "O"
            data.twothree = "occupied"
            data.XPatterns += "6"
            data.counter += 1
        elif 92 < event.x < 213 and 382 < event.y < 508 and data.threeone == "empty":
            data.XSlots.append((100, 390, 205, 495))
            data.XSlots.append((205, 390, 100, 495))
            data.turn = "O"
            data.threeone = "occupied"
            data.XPatterns += "7"
            data.counter += 1
        elif 237 < event.x < 358 and 382 < event.y < 508 and data.threetwo == "empty":
            data.XSlots.append((245, 390, 350, 495))
            data.XSlots.append((350, 390, 245, 495))
            data.turn = "O"
            data.threetwo = "occupied"
            data.XPatterns += "8"
            data.counter += 1
        elif 382 < event.x < 508 and 382 < event.y < 508 and data.threethree == "empty":
            data.XSlots.append((390, 390, 495, 495))
            data.XSlots.append((495, 390, 390, 495))
            data.turn = "O"
            data.threethree = "occupied"
            data.XPatterns += "9"
            data.counter += 1
        else:
            pass
    elif data.turn == "O":
        if 92 < event.x < 213 and 92 < event.y < 213 and data.oneone == "empty": # one one COMPLETE
            data.OSlots.append((100, 100, 205, 205))
            data.turn = "X"
            data.oneone = "occupied"
            data.OPatterns += "1"
            data.counter += 1
        elif 237 < event.x < 358 and 92 < event.y < 213 and data.onetwo == "empty": # one two COMPLETE
            data.OSlots.append((245, 100, 350, 205))
            data.turn = "X"
            data.onetwo = "occupied"
            data.OPatterns += "2"
            data.counter += 1
        elif 382 < event.x < 508 and 92 < event.y < 213 and data.onethree == "empty": # one three COMPLETE
            data.OSlots.append((390, 100, 495, 205))
            data.turn = "X"
            data.onethree = "occupied"
            data.OPatterns += "3"
            data.counter += 1
        elif 92 < event.x < 213 and 237 < event.y < 358 and data.twoone == "empty":
            data.OSlots.append((100, 245, 205, 350))
            data.turn = "X"
            data.twoone = "occupied"
            data.OPatterns += "4"
            data.counter += 1
        elif 237 < event.x < 358 and 237 < event.y < 358 and data.twotwo == "empty":
            data.OSlots.append((245, 245, 350, 350))
            data.turn = "X"
            data.twotwo = "occupied"
            data.OPatterns += "5"
            data.counter += 1
        elif 382 < event.x < 508 and 237 < event.y < 358 and data.twothree == "empty":
            data.OSlots.append((390, 245, 495, 350))
            data.turn = "X"
            data.twothree = "occupied"
            data.OPatterns += "6"
            data.counter += 1
        elif 92 < event.x < 213 and 382 < event.y < 508 and data.threeone == "empty":
            data.OSlots.append((100, 390, 205, 495))
            data.turn = "X"
            data.threeone = "occupied"
            data.OPatterns += "7"
            data.counter += 1
        elif 237 < event.x < 358 and 382 < event.y < 508 and data.threetwo == "empty":
            data.OSlots.append((245, 390, 350, 495))
            data.turn = "X"
            data.threetwo = "occupied"
            data.OPatterns += "8"
            data.counter += 1
        elif 382 < event.x < 508 and 382 < event.y < 508 and data.threethree == "empty":
            data.OSlots.append((390, 390, 495, 495))
            data.turn = "X"
            data.threethree = "occupied"
            data.OPatterns += "9"
            data.counter += 1
        else:
            pass
    if ("1" in data.XPatterns and "2" in data.XPatterns and "3" in data.XPatterns) \
        or ("4" in data.XPatterns and "5" in data.XPatterns and "6" in data.XPatterns) \
        or ("7" in data.XPatterns and "8" in data.XPatterns and "9" in data.XPatterns) \
        or ("1" in data.XPatterns and "4" in data.XPatterns and "7" in data.XPatterns) \
        or ("2" in data.XPatterns and "5" in data.XPatterns and "8" in data.XPatterns) \
        or ("3" in data.XPatterns and "6" in data.XPatterns and "9" in data.XPatterns) \
        or ("1" in data.XPatterns and "5" in data.XPatterns and "9" in data.XPatterns) \
        or ("7" in data.XPatterns and "5" in data.XPatterns and "3" in data.XPatterns):
        data.oneone = "occupied"
        data.onetwo = "occupied"
        data.onethree = "occupied"
        data.twoone = "occupied"
        data.twotwo = "occupied"
        data.twothree = "occupied"
        data.threeone = "occupied"
        data.threetwo = "occupied"
        data.threethree = "occupied"
        data.gameOver = "xWon"
        # drawX Won

    if ("1" in data.OPatterns and "2" in data.OPatterns and "3" in data.OPatterns) \
        or ("4" in data.OPatterns and "5" in data.OPatterns and "6" in data.OPatterns) \
        or ("7" in data.OPatterns and "8" in data.OPatterns and "9" in data.OPatterns) \
        or ("1" in data.OPatterns and "4" in data.OPatterns and "7" in data.OPatterns) \
        or ("2" in data.OPatterns and "5" in data.OPatterns and "8" in data.OPatterns) \
        or ("3" in data.OPatterns and "6" in data.OPatterns and "9" in data.OPatterns) \
        or ("1" in data.OPatterns and "5" in data.OPatterns and "9" in data.OPatterns) \
        or ("7" in data.OPatterns and "5" in data.OPatterns and "3" in data.OPatterns):
        data.oneone = "occupied"
        data.onetwo = "occupied"
        data.onethree = "occupied"
        data.twoone = "occupied"
        data.twotwo = "occupied"
        data.twothree = "occupied"
        data.threeone = "occupied"
        data.threetwo = "occupied"
        data.threethree = "occupied"
        data.gameOver = "oWon"
        # draw
    elif data.counter == 9:
        data.gameOver = "tie"
        print("yall suck,")

def playGameRedrawAll(canvas, data):
    canvas.create_text(data.width/2, 50,
                       text="It is " + data.turn + "'s" + " turn",
                       font="Arial 26 bold")
    canvas.create_text(data.width/2, 550,
                       text="HOME SCREEN", font="Arial 16 bold")
    canvas.create_rectangle(90, 90, 510, 510, outline="black")
    canvas.create_rectangle(230, 535, 370, 565, outline="black")
    # Board Rods
    canvas.create_rectangle(215, 100, 235, 500, fill="black") # vertical left
    canvas.create_rectangle(360, 100, 380, 500, fill="black")  # vertical right
    canvas.create_rectangle(100, 215, 500, 235, fill="black") # horizontal top
    canvas.create_rectangle(100, 360, 500, 380, fill="black") # horizontal bottom
    for slot in data.XSlots:
        canvas.create_line(slot, fill="#0651c9", width=8)
    for slot in data.OSlots:
        canvas.create_oval(slot, outline="red", width=8)
    if data.gameOver == "xWon":
        canvas.create_rectangle(50,150,550,450, fill="#7fbff0", state=data.show)
        canvas.create_rectangle(230, 350, 370, 390, outline="black", width=2, state=data.show)
        canvas.create_text(300,370, text="Back To Board!", font="Arial 18 bold", state=data.show)
        canvas.create_text(300,300, text="Player X Wins!", font="Arial 40 bold", state=data.show)
    elif data.gameOver == "oWon":
        canvas.create_rectangle(50,150,550,450, fill="#ed3e3e", state=data.show)
        canvas.create_rectangle(230, 350, 370, 390, outline="black", width=2, state=data.show)
        canvas.create_text(300,370, text="Back To Board!", font="Arial 18 bold", state=data.show)
        canvas.create_text(300,300, text="The Computer Wins!", font="Arial 40 bold", state=data.show)
    elif data.gameOver == "tie":
        canvas.create_rectangle(50,150,550,450, fill="#9e9b9b", state=data.show)
        canvas.create_rectangle(230, 350, 370, 390, outline="black", width=2, state=data.show)
        canvas.create_text(300,370, text="Back To Board!", font="Arial 18 bold", state=data.show)
        canvas.create_text(300,300, text="Cat's Game!", font="Arial 40 bold", state=data.show)



#%02x%02x%02x
################################
# Run
################################
def run(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)
