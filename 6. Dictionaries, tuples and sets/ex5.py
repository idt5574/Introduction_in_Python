d = dict([[i.split('=')[0], i.split('=')[1]] for i in input().split()])

if "house" in d and "True" in d and '5' in d:
    print("ДА")
else: print("НЕТ")

