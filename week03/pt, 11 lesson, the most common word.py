set = {}
n = int(input())
for i in range(n):
    line = input().split()
    for word in line:
        set[word] = set.get(word, 0) + 1

maxcounter = max(set.values())
mostcommon = [a for a, b in set.items() if b == maxcounter]
print(min(mostcommon))