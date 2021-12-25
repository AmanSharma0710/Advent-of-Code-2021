positions = list(map(int, input().split(",")))

minimum_position = min(positions)
maximum_position = max(positions)
answer= float('inf')
#just brute force the final position and take minimum of the fuel required
for final_position in range(minimum_position, maximum_position+1):
    current_answer = 0
    for i in positions:
        dis = abs(i-final_position)
        current_answer += (dis*(dis+1))/2
    answer = min(answer, current_answer)

print(answer)