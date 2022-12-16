import fileinput
import turtle
import time

v=0
def draw_board():
    pointer.penup()
    pointer.goto(2,6)
    pointer.pendown()
    pointer.goto(2,0)
    pointer.penup()
    pointer.goto(4,6)
    pointer.pendown()
    pointer.goto(4,0)
    pointer.penup()
    pointer.goto(0,4)
    pointer.pendown()
    pointer.goto(6,4)
    pointer.penup()
    pointer.goto(0,2)
    pointer.pendown()
    pointer.goto(6,2)
    pointer.penup()
def stamp_shape(x,y):
    global pointer, board
    global s
    global v
    if s%2 == 0:
        pointer.shape("circle")
        v = 2
    else:
        pointer.shape("turtle")
        v = 1
    if 0.1<x<1.9 and 4.1<y<5.9 and board[0][2] == 0:
        pointer.goto(1,5)
        pointer.stamp()
        board[0][2]=v
        s = s+1
    elif 0.1<x<1.9 and 2.1<y<3.9 and board[0][1] == 0:
        pointer.goto(1,3)
        pointer.stamp()
        board[0][1]=v
        s = s + 1
    elif 0.1<x<1.9 and 0.1<y<1.9 and board[0][0] == 0:
        pointer.goto(1,1)
        pointer.stamp()
        board[0][0]=v
        s = s + 1
    elif 2.1<x<3.9 and 4.1<y<5.9 and board[1][2] == 0:
        pointer.goto(3,5)
        pointer.stamp()
        board[1][2]=v
        s = s + 1
    elif 2.1<x<3.9 and 2.1<y<3.9 and board[1][1] == 0:
        pointer.goto(3,3)
        pointer.stamp()
        board[1][1]=v
        s = s + 1
    elif 2.1<x<3.9 and 0.1<y<1.9 and board[1][0] == 0:
        pointer.goto(3,1)
        pointer.stamp()
        board[1][0]=v
        s = s + 1
    elif 4.1<x<5.9 and 4.1<y<5.9 and board[2][2] == 0:
        pointer.goto(5,5)
        pointer.stamp()
        board[2][2]=v
        s = s + 1
    elif 4.1<x<5.9 and 2.1<y<3.9 and board[2][1] == 0:
        pointer.goto(5,3)
        pointer.stamp()
        board[2][1]=v
        s = s + 1
    elif 4.1<x<5.9 and 0.1<y<1.9 and board[2][0] == 0:
        pointer.goto(5,1)
        pointer.stamp()
        board[2][0]=v
        s = s + 1
    check_when()
def new_game():
    global board, pointer
    global s
    s = 0
    pointer.clearstamps()
    pointer.clear()
    draw_board()
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
def check_when():
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0:
        pointer.clear()
        if board[0][2] == 1:
            pointer.write("Turtle wins!")
        elif board[0][2] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0:
        pointer.clear()
        if board[0][1] == 1:
            pointer.write("Turtle wins!")
        elif board[0][1] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != 0:
        pointer.clear()
        if board[0][0] == 1:
            pointer.write("Turtle wins!")
        elif board[0][0] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != 0:
        pointer.clear()
        if board[1][0] == 1:
            pointer.write("Turtle wins!")
        elif board[1][0] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != 0:
        pointer.clear()
        if board[2][0] == 1:
            pointer.write("Turtle wins!")
        elif board[2][0] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[2][2] == board[1][2] and board[1][2] == board[0][2] and board[2][2] != 0:
        pointer.clear()
        if board[2][2] == 1:
            pointer.write("Turtle wins!")
        elif board[2][2] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        pointer.clear()
        if board[0][2] == 1:
            pointer.write("Turtle wins!")
        elif board[0][2] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        pointer.clear()
        if board[0][0] == 1:
            pointer.write("Turtle wins!")
        elif board[0][0] == 2:
            pointer.write("Circle wins!")
        screen.onkey(new_game, "n")
    elif board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 and board[1][1] != 0 and board [1][2] != 0 and board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0:
        pointer.clear()
        pointer.write("Draw")
        screen.onkey(new_game, "n")
def save_game():
    with open("TTT.txt","w") as f:
        f.write(str(board[0][2]))
        f.write(str(board[1][2]))
        f.write(str(board[2][2]))
        f.write(str(board[0][1]))
        f.write(str(board[1][1]))
        f.write(str(board[2][1]))
        f.write(str(board[0][0]))
        f.write(str(board[1][0]))
        f.write(str(board[2][0]))
        f.write(str(v))
    f.close()
    exit()
def load_game():
    with open("TTT.txt", "r") as f:
        board[0][2] = int(f.readline(1)[0])
        board[1][2] = int(f.readline(1)[0])
        board[2][2] = int(f.readline(1)[0])
        board[0][1] = int(f.readline(1)[0])
        board[1][1] = int(f.readline(1)[0])
        board[2][1] = int(f.readline(1)[0])
        board[0][0] = int(f.readline(1)[0])
        board[1][0] = int(f.readline(1)[0])
        board[2][0] = int(f.readline(1)[0])
        v = int(f.readline(1)[0])
        if v == 1:
            pointer.shape("circle")
        elif v == 2:
            pointer.shape("turtle")

nrl = input("Load game(L) or new game(N): ")
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
s = 1
v = 1

screen = turtle.Screen()
screen.setup(600,600)
screen.setworldcoordinates(0,0,6,6)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.shape("turtle")
pointer.shapesize(5,5)
pointer.penup()
pointer.pensize(15)
pointer.speed(0)

draw_board()
if nrl == "L" or nrl == "l":
    load_game()
    if board[0][2] != 0:
        if board[0][2] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(1, 5)
        pointer.stamp()
    if board[0][1] != 0:
        if board[0][1] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(1, 3)
        pointer.stamp()
    if board[0][0] != 0:
        if board[0][0] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(1, 1)
        pointer.stamp()
    if board[1][2] != 0:
        if board[1][2] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(3, 5)
        pointer.stamp()
    if board[1][1] != 0:
        if board[1][1] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(3,3)
        pointer.stamp()
    if board[1][0] != 0:
        if board[1][0] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(3,1)
        pointer.stamp()
    if board[2][2] != 0:
        if board[2][2] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(5,5)
        pointer.stamp()
    if board[2][1] != 0:
        if board[2][1] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(5,3)
        pointer.stamp()
    if board[2][0] != 0:
        if board[2][0] == 1:
            pointer.shape("turtle")
        else:
            pointer.shape("circle")
        pointer.goto(5,1)
        pointer.stamp()

while True:
    screen.onclick(stamp_shape)
    screen.onkey(save_game,"s")
    screen.listen()
    screen.mainloop()
