import turtle as t
import math
a = [1, 4, 1, 7, 0, 0]
t.shape("turtle")
t.speed(1)
t.turtlesize(0.5)
t.pensize(3)
t.speed(5)

def one():
    t.left(90)
    t.forward(40)
    t.left(135)
    t.forward(20 * math.sqrt(2))
    t.left(135)


def two():
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(180)
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(45)
    t.forward(20 * math.sqrt(2))
    t.left(135)
    t.forward(20)


def three():
    t.penup()
    t.left(135)
    t.forward(math.sqrt(500))
    t.right(135)
    t.pendown()
    t.forward(20)
    t.right(135)
    t.forward(20 * math.sqrt(2))
    t.left(135)
    t.forward(20)
    t.right(135)
    t.forward(20 * math.sqrt(2))
    t.left(135)


def four():
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(180)
    t.forward(40)
    t.right(90)


def five():
    t.penup()
    t.left(90)
    t.forward(40)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)


def six():
    t.penup()
    t.left(135)
    t.forward(20*math.sqrt(2))
    t.right(135)
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)


def seven():
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(180)
    t.pendown()
    t.forward(20)
    t.right(135)
    t.forward(20*math.sqrt(2))
    t.left(45)
    t.forward(20)
    t.left(90)


def eight():
    t.penup()
    t.left(135)
    t.forward(20 * math.sqrt(2))
    t.right(135)
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)


def nine():
    t.penup()
    t.left(180)
    t.forward(20)
    t.left(180)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)


def zero():
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)

i = 0
while i <= len(a):
    if a[i] == 1:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        one()
        i += 1
    elif a[i] == 2:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        two()
        i += 1
    elif a[i] == 3:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        three()
        i += 1
    elif a[i] == 4:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        four()
        i += 1
    elif a[i] == 5:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        five()
        i += 1
    elif a[i] == 6:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        six()
        i += 1
    elif a[i] == 7:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        seven()
        i += 1
    elif a[i] == 8:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        eight()
        i += 1
    elif a[i] == 9:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        nine()
        i += 1
    else:
        t.penup()
        t.goto(30 * i, 0)
        t.pendown()
        zero()
        i += 1
t.exitonclick()
