a = int(input())
b = int(input())
c = int(input())
if c >= a and b >= a:
    print(a)
elif c >= b and a >= b:
    print(b)
elif c <= b and c <= a:
    print(c)