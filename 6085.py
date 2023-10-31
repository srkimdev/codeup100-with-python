w, h, b = map(int, input().split())
print(format(w * h * b / 8 / 2**10 / 2**10, '.2f'), 'MB')