n = int(input())
su = 0

for i in range(3, n):
    su += i if i % 3 == 0 or i % 5 == 0 else 0

print(su)
