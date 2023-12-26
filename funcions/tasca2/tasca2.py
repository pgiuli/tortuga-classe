import turtle
turtle.speed(0)
turtle.pensize(3)

def edifici(pisos, habitacions):
    altura = 40 * pisos
    amplada = 40 * habitacions
    
    # Dibuixem el perimetre de l'edifici
    for _ in range(2):
        turtle.forward(amplada)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)
    
    for _ in range(pisos):
        turtle.pu()
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        for _ in range(habitacions):
            turtle.pu()
            turtle.forward(15)
            turtle.pd()
            for _ in range(2):
                turtle.forward(10)
                turtle.left(90)
                turtle.forward(20)
                turtle.left(90)
            turtle.pu()
            turtle.forward(25)
        turtle.pu()
        turtle.backward(amplada)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        
            
turtle.pu()
turtle.goto(-150, 0)
turtle.pd()
edifici(4, 2)
turtle.pu()
turtle.goto(80, 0)
turtle.pd()
edifici(2, 4)
turtle.done()