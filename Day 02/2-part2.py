depth = 0
horizontal = 0
aim = 0

while True:
    move = input().split()
    if len(move)<2:
        break
    if move[0] == 'down':
        aim += int(move[1])
    if move[0] == 'up':
        aim -= int(move[1])
    if move[0] == 'forward':
        horizontal += int(move[1])
        depth += aim* int(move[1])
print(depth*horizontal)