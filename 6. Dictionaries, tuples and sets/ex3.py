d = dict([[i.split('=')[0], int(i.split('=')[1])] for i in input().split()])
print(*sorted(d.items()))

