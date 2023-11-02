#입력
grid = [0 for _ in range(10)]

for i in range(10):
    grid[i] = list(map(int, input().split()))

x = y = 1

while True:
    

    if(grid[x][y] == 2):
        grid[x][y] = 9
        break
    elif(grid[x][y] == 0):
        grid[x][y] = 9

    if((grid[x+1][y] == 1 and grid[x][y+1] == 1) or (x == 9 and y == 9)):
        break

    if(grid[x][y+1] != 1):
        y += 1
    elif(grid[x+1][y] != 1):
        x += 1

    

for i in range(10):
    for j in range(10):
        print(grid[i][j], end = ' ')
    print()    