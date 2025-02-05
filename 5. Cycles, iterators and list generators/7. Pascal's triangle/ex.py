n = int(input())

triangle = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    print(' '.join(map(str, row)).center(width + 2))