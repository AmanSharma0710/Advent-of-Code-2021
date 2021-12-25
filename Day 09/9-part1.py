heatmap = []

while True:
    line = input()
    if line == "":
        break
    heatmap.append(list(map(int, list(line))))

risklevel = 0
for i in range(len(heatmap)):
    for j in range(len(heatmap[0])):
        lowpoint = True
        if j+1 < len(heatmap[0]):
            if heatmap[i][j] >= heatmap[i][j+1]:
                lowpoint = False
        if i+1 < len(heatmap):
            if heatmap[i][j] >= heatmap[i+1][j]:
                lowpoint = False
        if j-1 >= 0:
            if heatmap[i][j] >= heatmap[i][j-1]:
                lowpoint = False
        if i-1 >= 0:
            if heatmap[i][j] >= heatmap[i-1][j]:
                lowpoint = False
        if lowpoint:
            risklevel += heatmap[i][j]+1

print(risklevel)