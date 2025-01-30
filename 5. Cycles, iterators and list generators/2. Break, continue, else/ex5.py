ar = input().split()

i = 0
while i < len(ar):
    if ar[i][0].lower() == ar[i][-1]:
        print("ДА")
        break
    i += 1
else:
    print("НЕТ")
