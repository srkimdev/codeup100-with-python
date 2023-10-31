h, b, c, s = map(int, input().split())

a = h * b * c * s
print(format(a / 8 / 2**10 / 2**10, '.1f'), 'MB')