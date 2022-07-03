from hashlib import new
import turtle
import time
import random

hiz = 0.15
windows = turtle.Screen()
windows.title("Yılıan Oyunu")
windows.bgcolor("linen")
windows.setup(width=600, height=600)
windows.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue violet")
head.penup()
head.goto(0, 100)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("purple")
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

tails = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("black")
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Puan: {}'.format(puan), align='center', font=('Couier', 24, 'normal'))

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'

windows.listen()
windows.onkey(goUp, "Up")
windows.onkey(goDown, "Down")
windows.onkey(goRight, "Right")
windows.onkey(goLeft, "Left")

while(True):
    windows.update()
    
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = 'stop'
        for tail in tails:
            tail.goto(1000, 1000)
  
        tails =[]
        puan = 0
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Couier', 24, 'normal'))
        hiz = 0.15


    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        puan += 10
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Couier', 24, 'normal'))
        hiz -= 0.001

        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('violet')
        newTail.penup()
        tails.append(newTail)

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)
    
    move()
    time.sleep(hiz)