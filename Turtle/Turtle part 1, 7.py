import turtle as t
t.turtlesize(1)
t.shape("turtle")
t.color("gold", "black")
for i in range(5, 1000, 10):
    t.fd(i)
    t.left(90)
    t.fd(i)
    t.left(90)
    t.fd(i+5)
    t.left(90)
    t.fd(i+5)
    t.left(90)
t.exitonclick()
