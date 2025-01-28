m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

a, b, c = map(int, input().split())
print('#' if m[a - 1] == "фа" or m[a - 1] == "до" else '', m[a - 1],
      ' #' if m[b - 1] == "фа" or m[b - 1] == "до" else ' ', m[b - 1],
      ' #' if m[c - 1] == "фа" or m[c - 1] == "до" else ' ', m[c - 1], sep='')
