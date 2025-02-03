import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for i, line in enumerate(lst_in):
    while '  ' in line:
        line = line.replace('  ', ' ')
    line = line.replace(' ', '-')
    lst_in[i] = line

for line in lst_in:
    print(line)
