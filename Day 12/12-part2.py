from collections import defaultdict
adj = defaultdict(list)
while True:
    line = input()
    if line == "":
        break
    x, y = line.split("-")
    adj[x].append(y)
    adj[y].append(x)

def isSmall(x):
    return x.islower()

def dfs(x, visited, taken_twice):
    paths = 0
    for y in adj[x]:
        if y=="end":
            paths+=1
            continue
        if y not in visited:
            new_visited = visited.copy()
            if isSmall(y):
                new_visited.add(y)
            paths += dfs(y, new_visited, taken_twice)
        if y in visited and taken_twice==0:
            if y=="start":
                continue
            paths+= dfs(y, visited, 1)
    return paths

already_visited = set()
already_visited.add("start")
print(dfs("start", already_visited, 0))