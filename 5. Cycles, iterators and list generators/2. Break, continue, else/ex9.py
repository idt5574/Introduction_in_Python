import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

i = 0
while i < len(lst_in):
    if ' ' in lst_in[i]:
        lst_in.remove(lst_in[i])
        continue
    i += 1

print(*lst_in)
