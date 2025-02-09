import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
t_lst_in = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]

for x in t_lst_in:
    print(*x)

