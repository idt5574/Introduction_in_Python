import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict([[int(i.split('=')[0]), i.split('=')[1]] for i in lst_in])
print(*sorted(d.items()))

