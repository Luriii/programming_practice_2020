a = int(input())
b = int(input())
if a < b:
    a, b = b, a
x = int(input())
while x != 0:
    if x > a:
        b, a = a, x
    elif x > b:
        b = x
    x = int(input())
print(b)