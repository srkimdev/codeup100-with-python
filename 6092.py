n = int(input())
a = list(map(int, input().split()))

result = []

for i in range(24):
    result.append(0)

for i in range(n):
    result[a[i]] += 1

for i in range(1, 24):
    print(result[i], end = ' ')