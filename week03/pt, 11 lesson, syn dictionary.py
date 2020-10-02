num = int(input())
syn= {}
for i in range(num):
    first, second = input().split()
    syn[first] = second
    syn[second] = first
print(syn[input()])