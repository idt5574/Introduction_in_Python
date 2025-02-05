ar = list(map(int, input().split()))

for i in range(len(ar)):
    swapped = False
    for j in range(len(ar) - 1):
        if ar[j] > ar[j + 1]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
            swapped = True
    
    if not swapped:
        break

print(*ar)
    