heatmap = []

while True:
    line = input()
    if line == "":
        break
    heatmap.append(list(map(int, list(line))))

visited = [[False for i in range(len(heatmap[0]))] for j in range(len(heatmap))]
for i in range(len(heatmap)):
    for j in range(len(heatmap[0])):
        if heatmap[i][j] == 9:
            heatmap[i][j] = 0
        else :
            heatmap[i][j] = 1

def dfs(x, y):
    if heatmap[x][y] == 0:
        return 0
    if visited[x][y]:
        return 0
    visited[x][y] = True
    basin = 1
    if x+1 < len(heatmap):
        basin += dfs(x+1, y)
        dfs(x+1, y)
    if y+1 < len(heatmap[0]):
        basin += dfs(x, y+1)
        dfs(x, y+1)
    if x-1 >= 0:
        basin += dfs(x-1, y)
        dfs(x-1, y)
    if y-1 >= 0:
        basin += dfs(x, y-1)
        dfs(x, y-1)
    return basin
    
    

basinsize = []
for i in range(len(heatmap)):
    for j in range(len(heatmap[0])):
        if not visited[i][j] and heatmap[i][j] == 1:
            basin = dfs(i, j)
            basinsize.append(basin)
basinsize.sort(reverse=True)
print(basinsize[0]*basinsize[1]*basinsize[2])

