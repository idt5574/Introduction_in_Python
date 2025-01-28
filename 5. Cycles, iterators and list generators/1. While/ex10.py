n = int(input())
x = 1000

i = 0
while i < n:
    x *= 1.05
    i += 1

print(round(x, 2))
