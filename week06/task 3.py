import math


def circle(r):
    return math.pi * r ** 2


def rectangle(a, b):
    return a * b


def triangle(a, b, angle):
    return 0,5 * a * b * math.sin(angle)


userschoice = input("triangle, rectangle and circle: ")
if userschoice == 'circle':
    radius = float(input("radius: "))
    print("Площадь круга: " + str(circle(radius)))
elif userschoice == 'rectangle':
    l = float(input("length: "))
    w = float(input("width: "))
    print("Площадь прямоугольника: " + str(rectangle(w*l)))
elif userschoice == 'triangle':
    a = float(input("a: "))
    b = float(input("b: "))
    angle = float(input("angle: "))
    print("Площадь треугольника: " + str(triangle(a, b, angle)))


