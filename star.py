import turtle
pen = turtle.Turtle()
pen.color('red', 'yellow')
pen.begin_fill()
while True:
    pen.forward(200)
    pen.left(170)
    if abs(pen.pos()) < 1:
        break
pen.end_fill()
screen = turtle.Screen()
screen.exitonclick()
