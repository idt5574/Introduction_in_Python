ar = list(map(float, input().split()))

for i, d in enumerate(ar):
    if d < 0:
        ar[i] = -1.0

print(*ar)
