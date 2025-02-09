n = int(input())

lst = [[0 if j != i else 1 for j in range(n)] for i in range(n)]

for x in lst:
    print(*x)

