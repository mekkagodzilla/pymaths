import turtle

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

def star(n):
    for pouetpouet in range(5):
        turtle.forward(n)
        turtle.right(144)


def starSpiral(initial_size, iterations, angle, increase):

    for i in range(iterations):
        star(initial_size)
        turtle.right(angle)
        initial_size += increase


starSpiral(20, 60, 5, 5)

string ='I made a change.'

turtle.exitonclick()
