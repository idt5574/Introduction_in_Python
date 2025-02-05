import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

for i in range(0, len(lst_in)):
    for j in range(i + 1, len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            break
    else: continue
    print("НЕТ")
    break
else:
    print("ДА")
