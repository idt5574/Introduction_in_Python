ar = input().lower().split()

for i in range(len(ar) - 1):
    if ar[i][-1] in "ьъы":
        if ar[i + 1][0] != ar[i][-2]:
            print("НЕТ")
            break
    else:
        if ar[i + 1][0] != ar[i][-1]:
            print("НЕТ")
            break   
else: print("ДА")
