p = [0] * 10

while p.count(1) < 5:
    index = int(input())
    if p[index] == 0:
        p[index] = 1

print(*p)
