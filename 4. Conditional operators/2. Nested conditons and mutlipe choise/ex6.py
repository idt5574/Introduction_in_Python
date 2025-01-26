m, n = map(int, input().split())

dd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n == 1:
    print(f"{str(m - 1).rjust(2, '0')}.{dd[m - 1]}", end=' ')
else:
    print(f"{str(m).rjust(2, '0')}.{n - 1}", end=' ')

if n == dd[m - 1]:
    print(f"{str(m + 1).rjust(2, '0')}.01")
else:
    print(f"{str(m).rjust(2, '0')}.{str(n + 1).rjust(2, '0')}")
