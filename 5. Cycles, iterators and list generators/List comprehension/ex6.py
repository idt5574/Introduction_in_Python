n = int(input())

lst = [[i for j in range(n)] for i in range(n)]

for x in lst:
    print(*x)

