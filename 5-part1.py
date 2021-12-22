lines = []
while True:
    next_line = input()
    if next_line == "":
        break
    parts = next_line.split(" -> ")
    from_point = parts[0].split(",")
    to_point = parts[1].split(",")
    if from_point[0]==to_point[0] or from_point[1]==to_point[1]:
        lines.append([from_point, to_point])

points = []
for line in lines:
    from_point = line[0]
    to_point = line[1]
    if from_point[0]==to_point[0]:
        for y in range(min(int(from_point[1]), int(to_point[1])), max(int(from_point[1]), int(to_point[1]))+1):
            points.append((int(from_point[0]), y))
    elif from_point[1]==to_point[1]:
        for x in range(min(int(from_point[0]), int(to_point[0])), max(int(from_point[0]), int(to_point[0]))+1):
            points.append((x, int(from_point[1])))

from collections import Counter
counts = Counter(points)
overlapping =0
for point in counts:
    if counts[point]>1:
        overlapping +=1
    

print(overlapping)