lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for i in lst_in:
    if i.split()[1] in d:
        d[i.split()[1]].append(i.split()[0])
        continue

    d[i.split()[1]] = [i.split()[0]]

print(*sorted(d.items()))

