lst = list(input().split())
d = {}

for i in lst:
    if i[:2] in d:
        d[i[:2]].append(i)
        continue

    d[i[:2]] = [i]

print(*sorted(d.items()))

