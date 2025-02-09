a = list(map(int, input().split()))
n = 0
for i in range(1, len(a)):
    if len(a) // i == i:
        n = i
        break

print([[a[j] for j in range(i, i + n)] for i in range(0, len(a), n)])

