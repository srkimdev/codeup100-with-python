# 세로h, 가로w
# 막대의 개수 n
# 길이l, 방향d, x, y

h, w = map(int, input().split())

grid = []

for i in range(h+1):
    grid.append([])
    for j in range(w+1):
        grid[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    if (d == 0):
        for j in range(l):
            grid[x][y+j] = 1
    else:
        for j in range(l):
            grid[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(grid[i][j], end = ' ')
    print()