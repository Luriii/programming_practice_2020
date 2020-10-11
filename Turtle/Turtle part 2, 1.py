import turtle as t
from random import *
t.shape("turtle")
t.bgcolor("orange")
t.color("chocolate")
t.speed(300)
for i in range(10000):
    n = randint(0, 1)
    if n == 0:
        t.left(randint(0, 360))
    else:
        t.right(int(randint(0, 360)))
    t.forward(randint(0, 50))
