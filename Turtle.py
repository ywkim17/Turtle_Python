from turtle import *

# Set Turtle Screen
screen = Screen()
screen.screensize(800, 500)
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")

# Set Pen
pen = Turtle()
pen.hideturtle()
pen.color("red")
pen.pensize(3)
pen.speed(10)

# Set Pen Position
def goto(x, y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

# Draw I
goto(-600,200)
pen.right(90)
pen.forward(200)

# Draw L
goto(-500,200)
pen.forward(200)
pen.left(90)
pen.forward(100)

# Draw O
pen.speed(20)
goto(-280,15)

def talloval(r):               # Verticle Oval
    pen.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        pen.circle(r,90)    # Long curved part
        pen.circle(r/2,90)

talloval(115)
pen.speed(10)

# Draw V
goto(-220, 200)
pen.left(240)
pen.forward(210)
pen.left(150)
pen.forward(210)

# Draw E
goto(50, 200)
pen.right(255)
pen.forward(100)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(100)
goto(-50, 100)
pen.forward(100)

# Draw Y
goto(150, 200)
pen.right(60)
pen.forward(120)
pen.left(125)
pen.forward(120)
pen.backward(120)
pen.right(155)
pen.forward(100)

# Draw O
pen.speed(20)
goto(380, 10)
pen.left(90)
talloval(115)

# Draw U
goto(450, 200)
pen.right(135)
pen.forward(140)
pen.circle(70,180)
pen.forward(140)

done()