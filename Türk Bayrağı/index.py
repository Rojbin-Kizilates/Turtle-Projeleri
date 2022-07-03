from turtle import *
title("Türk Bayrağı")
setup(width=600, height=400)
bgcolor("red")
hideturtle()
def colorAndLocation(renk, x, y):
    penup()
    goto(x, y)
    pendown()
    color(renk)
    begin_fill()
def star():
    colorAndLocation("white", 80, 25)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()

def moon(cap):
    circle(cap)
    end_fill()
colorAndLocation('white', -110, -120)
moon(130)
colorAndLocation("red", -70, -90)
moon(100)
star()
mainloop()