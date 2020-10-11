import turtle as t
t.shape("turtle")
t.bgcolor("black")
t.color("white")
t.penup()
t.goto(-200, 0)
t.pendown()
t.left(90)
x = 1
while x < 11:
    t.circle(-20, 180)
    t.circle(-5, 180)
t.exitonclick()
