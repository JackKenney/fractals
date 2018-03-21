import turtle, time
PROGNAME = 'Sierpinski Carpet'
#Credits: This code was written by editing the code from http://www.lpb-riannetrujillo.com/blog/python-fractal/

myPen = turtle.Turtle()
turtle.screensize(bg='yellow')
myPen.speed(0)
myPen.hideturtle()
myPen.color("green")


# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)

def carpet(point, size, depth):
    #Position myPen in center of the screen
    myPen.penup()
    myPen.goto(point[0], point[1])
    myPen.pendown()
    # draw me
    box(size)
    if depth > 0:
        # top left
        start = (
            point[0] - (2/3) * size,
            point[1] + (4/3) * size,
        )
        carpet(start, size/3, depth-1)
        # top middle
        start = (
            point[0] + (1/3) * size,
            point[1] + (4/3) * size,
        )
        carpet(start, size/3, depth-1)
        # top right
        start = (
            point[0] + (4/3) * size,
            point[1] + (4/3) * size,
        )
        carpet(start, size/3, depth-1)
        # left
        start = (
            point[0] - (2/3) * size,
            point[1] + (1/3) * size,
        )
        carpet(start, size/3, depth-1)
        # right
        start = (
            point[0] + (4/3) * size,
            point[1] + (1/3) * size,
        )
        carpet(start, size/3, depth-1)
        # bottom left
        start = (
            point[0] - (2/3) * size,
            point[1] - (2/3) * size,
        )
        carpet(start, size/3, depth-1)
        # bottom middle
        start = (
            point[0] + (1/3) * size,
            point[1] - (2/3) * size,
        )
        carpet(start, size/3, depth-1)
        # bottom right
        start = (
            point[0] + (4/3) * size,
            point[1] - (2/3) * size,
        )
        carpet(start, size/3, depth-1)
    # else:
    #     time.sleep(50)

LAYERS = 4
SIZE = 243

carpet((-125, -125), SIZE, LAYERS)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="carpet.eps")
