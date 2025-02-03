s = input()

it = iter(s)

while (x := next(it)) != ' ':
    print(x, end='')
