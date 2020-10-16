def not_main(matrix):

    return print(sum(matrix[i][length - 1 - i] for i in range(length)))


def main(matrix):
    return print(sum(matrix[i][i] for i in range(length)))


matrix = []
length = int(input())
for i in range(length):
    matrix.append([])
    k = list(map(int, input().split()))
    for j in range(length):
        matrix[i].append(k[j])
initialchoice = input('What are we going to count: main or not main?')
if initialchoice == 'main':
    main(matrix)

elif initialchoice == 'not main':
    not_main(matrix)
