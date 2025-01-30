n = int(input())

ar = []

i = 1
while i < n + 1:
    if n > 99:
        print("слишком большое значение n")
        break
    
    if i % 3 == 0 and i % 5 == 0:
        ar.append(i)
    
    i += 1
else:
    print(*ar)