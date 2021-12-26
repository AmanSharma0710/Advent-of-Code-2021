grid = []
while True:
    line = input()
    if line == '':
        break
    grid.append(list(map(int, list(line))))
grid[0][0] = 0
n = len(grid)
m = len(grid[0])
visited = [[False for _ in range(m)] for _ in range(n)]
import heapq
heap = []
heapq.heappush(heap, (0, (0, 0)))
visited[0][0] = True
while True:
    weight, point = heapq.heappop(heap)
    if point == (n - 1, m - 1):
        print(weight)
        break
    for i, j in [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]:
        if 0 <= i < n and 0 <= j < m and not visited[i][j]:
            heapq.heappush(heap, (grid[i][j] + weight, (i, j)))
            visited[i][j] = True

