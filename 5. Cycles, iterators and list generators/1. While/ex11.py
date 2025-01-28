n, m = map(int, input().split())
n += n % 2 == 0

while n < m + 1:
    print(n, end=' ')
    n += 2
