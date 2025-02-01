ar = list(map(int, input().split()))

skip = False

for i, d in enumerate(ar):
    if skip:
        skip = False
        continue

    ar.insert(i + 1, d)
    skip = True

print(*ar)