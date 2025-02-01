s = input()
isFinded = False


for i in range(len(s) - 1):
    if s[i] == 'р' and s[i + 1] == 'а':
        print(i, end=' ')
        isFinded = True
    
if not isFinded:
    print(-1)
