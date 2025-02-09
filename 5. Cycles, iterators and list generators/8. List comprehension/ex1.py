lst = list(map(float, input().split()))
lst_abs = [x if x >= 0 else -x for x in lst]
print(lst_abs)

