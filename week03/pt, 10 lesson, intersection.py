A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])
C = sorted(list(A.intersection(B)))
print(' '.join([str(i) for i in C]))
