ar = input().split()

i = 0
while i < len(ar):
    if(len(ar[i]) < 6):
        print("НЕТ")
        break
    
    i += 1
else:
    print("ДА")
