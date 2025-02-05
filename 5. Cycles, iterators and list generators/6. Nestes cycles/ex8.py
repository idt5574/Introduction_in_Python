n = int(input())
ar = [1, 2, 4, 8, 16, 64]

x = 0
index = 5

while x != n:

    if x + ar[index] > n:
        index -= 1
        continue
    
    x += ar[index]
    print(ar[index], end=' ')
