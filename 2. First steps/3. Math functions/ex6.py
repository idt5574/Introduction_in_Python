import math

n, k = map(int, input().split())
C = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(int(C))
