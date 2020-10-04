import turtle as t
import math
t.shape('turtle')
t.bgcolor("black")
t.color("gold", "olive")
n = 3
r = 10
def angle(n, m):
    q = 360 / n
    while n > 0:
        t.left(q)
        t.forward(m)
        n -= 1
while n < 13:
    m = 2 * r * math.sin(math.pi/n)
    x = (180 - 360/n)/2
    t.left(x)
    angle(n, m)
    t.right(x)
    t.penup()
    t.forward(10)
    t.pendown()
    n += 1
    r += 10
turtle.exitonclick()

