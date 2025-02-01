form = "+7(xxx)xxx-xx-xx"
s = input()

for i, d in enumerate(s):
    if (form[i] != 'x' and form[i] != d) or (form[i] == 'x' and not d.isdigit()):
        print("НЕТ")
        break
else:
    print("ДА")
