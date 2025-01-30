mult = 1

while True:
    x = int(input())

    if(x < 0): continue
    elif(x == 0): break
    mult *= x

print(mult)
    