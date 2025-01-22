lst = list(map(int, input().split()))
lst[-1] = lst[-1] % 2 != 0
print(*lst)
