n = int(input())
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''.split('\n')

if n == 1:
    print(m[0])
elif n == 2:
    print(m[1])
elif n == 3:
    print(m[2])
elif n == 4:
    print(m[3])
elif n == 5:
    print(m[4])
elif n == 6:
    print(m[5])
