import turtle
turtle.shape('turtle')
turtle.delay(0)
def square(n):
    """Draws a square of side n."""
    for a in range(4):
        turtle.forward(n)
        turtle.right(90)


def triangle(n):
    for i in range(3):
        turtle.forward(n)
        turtle.left(120)

def hexagon(n):
    for i in range(6):
        turtle.forward(n)
        turtle.left(60)

side = 3
for i in range(72):
    hexagon(side)
    turtle.left(5)
    side += 3

turtle.exitonclick()