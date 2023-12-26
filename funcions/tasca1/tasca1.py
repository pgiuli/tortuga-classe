import turtle
import random
turtle.color('red', 'yellow')
turtle.pensize(5)
def polygon():
    sides = random.randint(3, 10)
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)

polygon()
turtle.done()