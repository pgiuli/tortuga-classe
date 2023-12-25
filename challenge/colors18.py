import turtle
colors = ['red', 'purple', 'blue', 'green']
turtle.pu()
turtle.speed(10)
turtle.pensize(5)
turtle.goto(-150,150)
for _ in range(4):
    for i in range(4):
        turtle.pd()
        turtle.color(colors[i])
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(50)
        turtle.pu()
        turtle.forward(50)
    turtle.backward(50)
    turtle.rt(90)
    turtle.forward(50)

# Less lines
    
import turtle
colors = ['red', 'purple', 'blue', 'green']
turtle.pu()
turtle.goto(-150,150)
for _ in range(4):
    for i in range(4):
        turtle.pd()
        turtle.color(colors[i])
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