grid = []
for i in range(10):
    grid.append(list(map(int, list(input()))))

flashed= [[False for i in range(10)] for j in range(10)]

def flash(x, y):
    if grid[x][y]>9 and not flashed[x][y]:
        flashed[x][y]=True
        if x+1<10:
            grid[x+1][y]+=1
            flash(x+1, y)
        if y+1<10:
            grid[x][y+1]+=1
            flash(x, y+1)
        if x-1>=0:
            grid[x-1][y]+=1
            flash(x-1, y)
        if y-1>=0:
            grid[x][y-1]+=1
            flash(x, y-1)
        if x+1<10 and y+1<10:
            grid[x+1][y+1]+=1
            flash(x+1, y+1)
        if x-1>=0 and y-1>=0:
            grid[x-1][y-1]+=1
            flash(x-1, y-1)
        if x+1<10 and y-1>=0:
            grid[x+1][y-1]+=1
            flash(x+1, y-1)
        if x-1>=0 and y+1<10:
            grid[x-1][y+1]+=1
            flash(x-1, y+1)
        return
    return
iteration = 0
while True:
    numberOfFlashes=0
    iteration += 1
    for i in range(10):
        for j in range(10):
            flashed[i][j]=False
            grid[i][j] += 1
    for i in range(10):
        for j in range(10):
            flash(i, j)
    for i in range(10):
        for j in range(10):
            if grid[i][j]>9:
                numberOfFlashes+=1
                grid[i][j]=0
    if numberOfFlashes==100:
        break

print(iteration)