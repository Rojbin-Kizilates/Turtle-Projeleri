import turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(0)
turtle.bgcolor("black")
for i in range(6):
    for colors in ["red", "pink", "purple", "blue", "cyan", "white"]:
        t.color(colors)
        t.circle(100)
        t.left(10)
t.hideturtle()

