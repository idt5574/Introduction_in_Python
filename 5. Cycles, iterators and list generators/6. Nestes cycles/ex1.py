n = int(input())

ar = []

for i in range(n):

    t = []

    for j in range(n):
        t.append(1 if j != n - 1 else 5)
    
    ar.append(t)

for i in ar:
    print(*i)
