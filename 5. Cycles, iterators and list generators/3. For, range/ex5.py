ar = list(map(int, input().split()))

su = 0
for i in ar:
    if i % 2 != 0:
        su += i
    
print(su)
