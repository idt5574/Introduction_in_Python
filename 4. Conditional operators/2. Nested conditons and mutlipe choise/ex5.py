n = int(input())

if (n <= 7 and n % 2 != 0) or (n > 7 and n % 2 == 0):
    print(31)
elif n == 2:
    print(28)
else:
    print(30)
