d = {}

while True:
    x = int(input())

    if x == 0: 
        break

    if x in d:
        print("значение из кэша:", round(d[x], 2))
        continue

    d[x] = x ** 0.5
    print(round(d[x], 2))

