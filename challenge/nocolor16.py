import turtle
turtle.pu()
turtle.goto(-150,150)
turtle.speed(10)
turtle.pensize(5)
for _ in range(4):
    for _ in range(4):
        turtle.pd()
        for _ in range(2):
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(50)
        turtle.pu()
        turtle.forward(50)
    turtle.backward(50)
    turtle.rt(90)
    turtle.forward(50)
    