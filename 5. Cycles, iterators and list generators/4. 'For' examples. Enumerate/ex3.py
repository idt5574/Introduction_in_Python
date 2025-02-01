text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))
