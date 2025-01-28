s = input()

i, res = 0, 1
while i < len(s):
    res *= int(s[i])
    i += 1

print(res)
