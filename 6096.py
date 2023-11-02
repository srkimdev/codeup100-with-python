
d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(1, 20):
        if(d[j][y] == 0):
            d[j][y] = 1
        else:
            d[j][y] = 0

    for k in range(1, 20):
        if(d[x][k] == 0):
            d[x][k] = 1
        else:
            d[x][k] = 0


for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()

