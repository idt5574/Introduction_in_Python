a, b, c = map(int, input().split())
x = (a + b > c) and (a + c > b) and (b + c > a)
print(x)
