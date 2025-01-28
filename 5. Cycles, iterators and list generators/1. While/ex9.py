n = int(input())
res = 1

i = 1
while i < n + 1:
    res *= 2 if i % 3 == 0 else 1
    i += 1

print(res)
