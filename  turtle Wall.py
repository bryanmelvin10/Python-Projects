import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.setworldcoordinates(0, 0, 400, 400)

pointer = turtle.Turtle()
pointer.up()
pointer.hideturtle()
pointer.speed(0)


def drawRect(x, y, length, height):
    pointer.up()
    pointer.goto(x, y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x + length, y)
    pointer.goto(x + length, y + height)
    pointer.goto(x, y + height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()


def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
    indent = True
    h = 10
    for i in range(0,rows):

        if indent == True:
            w = 10 + brickWidth+(mortarWidth/2)-(brickWidth/2)-mortarWidth + mortarWidth
            drawRect(10, h, brickWidth+(mortarWidth/2)-(brickWidth/2)-mortarWidth, brickHeight)
            for i in range(0,cols-1):
                drawRect(w, h, brickWidth, brickHeight)
                w = w + mortarWidth + brickWidth
            drawRect(w, h, brickWidth+(mortarWidth/2)-(brickWidth/2)-mortarWidth, brickHeight)
            indent = False
        else:
            w = 10
            for i in range(0,cols):
                drawRect(w, h, brickWidth, brickHeight)
                w = w + mortarWidth + brickWidth
                indent = True
        h = h + mortarWidth + brickHeight


def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    h = 10
    for i in range(0,rows):
        w = 10
        for i in range(0,cols):
            drawRect(w, h, brickWidth, brickHeight)
            w = w + mortarWidth + brickWidth
        h = h + mortarWidth + brickHeight

rows = int(input("how many rows you want: "))
cols = int(input("how many columns do you want: "))
brickWidth = int(input("how big do you want the brick Width: " ))
brickHeight = int(input("how big do you want the height of the brick: "))
mortarWidth = int(input("how big do you want the mortar height: "))
wall = input("How do you want to build the wall fancy or simple: ")
if wall.lower() == "fancy":
    drawBrickWallOffset(rows,cols,brickWidth,brickHeight,mortarWidth)
if wall.lower() == "simple":
    drawBrickWall(rows,cols,brickWidth,brickHeight,mortarWidth)
