positions = list(map(int, input().split(",")))

import statistics
final_position = statistics.median(positions)

answer=0
for i in positions:
    answer += abs(i-final_position)

print(answer)