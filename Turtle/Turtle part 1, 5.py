import turtle
n = int(input())
turtle.shape("turtle")
turtle.color("#dd2fe0")
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360+360/n)
turtle.exitonclick()