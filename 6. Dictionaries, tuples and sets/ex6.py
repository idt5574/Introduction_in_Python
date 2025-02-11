d = dict([[i.split('=')[0], i.split('=')[1]] for i in input().split()])

if "False" in d:
    del d["False"]

if "3" in d:
    del d["3"]

print(*sorted(d.items()))

