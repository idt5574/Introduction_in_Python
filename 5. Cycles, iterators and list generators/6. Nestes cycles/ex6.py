ar = list(map(int, input().split()))

for i in range(len(ar) - 1):
    mi = 10000
    ind = 0
    for j in range(i + 1, len(ar)):
        if ar[j] < mi:
            mi = ar[j]
            ind = j
    ar[i], ar[ind] = ar[ind], ar[i]
    
print(*ar)
