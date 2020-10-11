import turtle as t
t.shape("turtle")
t.bgcolor("lightblue")
t.color("yellow")
i = 1
n = 6  # Количество лепестков


def myflower(i):
  while i <= n:
    t.circle(50)
    t.left(360 / n)
    i += 1


myflower(i)
t.exitonclick()
