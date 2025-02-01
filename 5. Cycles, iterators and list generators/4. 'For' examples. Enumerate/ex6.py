ar = list(map(float, input().split()))

mi = 100000.0
for i in ar:
    if i < mi:
        mi = i

print(mi)
