a, m, d, n = map(int, input().split())
result = 1

for i in range(1, n):
    if (i == 1):
        result = a * m + d
    else:
        result = result * m + d
print(result)