ar = list(map(int, input().split()))

for i, d in enumerate(ar):
    ar[i] = d**2

print(*ar)
