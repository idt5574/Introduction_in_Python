n = int(input())

i = 2
ar = [1, 1]
print(*ar, end=' ')
while i < n:
    su = sum(ar)
    print(su, end=' ')
    ar[0], ar[1] = ar[1], su
    i += 1
