a = [int(i) for i in input().split()]
maxindex = 0
minindex = 0
for i in range(1, len(a)):
    if a[i] > a[maxindex]:
        maxindex = i
    if a[i] < a[minindex]:
        minindex = i
a[minindex], a[maxindex] = a[maxindex], a[minindex]
print(' '.join([str(i) for i in a]))