a = [int(s) for s in input().split()]
b = [int(q) for q in input().split()]
length = 0
if len(a) >= len(b):
    length = len(a)
else:
    length = len(b)
for i in range(length):
    c = a[i]
    d = b[i]
    while c != 0 and d != 0:
        if c > d:
            c %= d
        else:
            d %= c
    gcd = c + d
    print(gcd, end=" ")

