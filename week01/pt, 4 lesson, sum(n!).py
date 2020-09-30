res = 1
x = 0
n = int(input())
for i in range(1,n+1):
    res *= i
    x += res
print(x)
