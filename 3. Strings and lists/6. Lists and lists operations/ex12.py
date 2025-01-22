cities = ["Москва", "Тверь", "Вологда"]
print(*(cities + list(map(str, input().split()))))
