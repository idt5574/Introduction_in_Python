slag = input()

while "--" in slag:
    slag = slag.replace("--", "-")

print(slag)