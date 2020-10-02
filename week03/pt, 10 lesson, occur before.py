a = [int(i) for i in input().split()]
they_were_before = set()
for i in a:
    if i in they_were_before:
        print("YES")
    else:
        print("NO")
        they_were_before.add(i)