import turtle as t
t.shape("turtle")
t.bgcolor("midnightblue")
t.speed(100)
n = 5  # Количество вершин
t.penup()
t.goto(-100, 0)
t.pendown()


def stars(n):
    t.left(180 - (180 / n))
    t.forward(200)


x = 1
t.fillcolor("yellow")
t.begin_fill()
while x <= n:
    stars(n)
    x += 1
t.end_fill()
t.penup()
t.goto(150, 0)
t.pendown()
x = 1
m = 11
t.fillcolor("yellow")
t.begin_fill()
while x <= m:
    stars(m)
    x += 1
t.end_fill()
t.exitonclick()
