from turtle import*
import math as m

shape("turtle")
speed(10)

def triangle(size):
    if size > 100000:
        return
    forward(m.sqrt(size))
    left(90)    
    triangle(size+1)

triangle(100)

mainloop()