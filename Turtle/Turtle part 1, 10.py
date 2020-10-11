import turtle as t
t.shape("turtle")
t.bgcolor("olive")
t.color("gold")
t.left(90)
x = 0
n = 20


def butterfly(n):  # Функция, рисующая бабочку
    t.circle(n)
    t.circle(-n)


while x <= 20:
    butterfly(n)
    n += 10
    x += 1
t.exitonclick()
