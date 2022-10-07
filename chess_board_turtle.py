#using Turtle library
import turtle as t

step = 40

for i in range (8):
    for j in range(8):        
        t.penup()
        t.goto(step *j, step * i)
        t.pendown()
        if (j + i) % 2 == 0:
            t.color("black", "black")
        else:
            t.color("black", "white")
        t.begin_fill()
        for k in range(4):
            t.forward(step)
            t.left(90)
        t.end_fill()
t.done()