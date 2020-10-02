text = set()
a = int(input())
for i in range(a):
    text.update(input().split())
print(len(text))
