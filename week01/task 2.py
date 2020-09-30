n = int(input())
text = input()
for i in range(n):
    if i == 0:
        print("Hello,"+text, end=", ")
    if i < (n-1):
        print(text, end=", ")
    else:
        print(text)