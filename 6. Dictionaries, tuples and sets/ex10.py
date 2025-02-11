import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for i in lst_in:
    if i in d:
        print("Взято из кэша:", d[i])
        continue

    d[i] = "HTML-страница для адреса " + i;
    print(d[i])

