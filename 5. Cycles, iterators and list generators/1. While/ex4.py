n = int(input())
res = 0

i = 1
while i < n + 1:
    res += 1 / i
    i += 1

print(round(res, 3))
