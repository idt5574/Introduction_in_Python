ar = input().split()

if "Москва" in ar:
    ar.remove("Москва")

print(*ar)
