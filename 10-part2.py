incomplete = []
while True:
    line = input()
    if line == "":
        break
    stack = []
    corrupted = False
    i=0
    for i in range(len(line)):
        if line[i] in ['(', '{', '[', '<']:
            stack.append(line[i])
        elif line[i] in [')', '}', ']', '>']:
            if len(stack) == 0:
                break
            if line[i] == ')' and stack[-1] != '(':
                corrupted = True
                break
            if line[i] == '}' and stack[-1] != '{':
                corrupted = True
                break
            if line[i] == ']' and stack[-1] != '[':
                corrupted = True
                break
            if line[i] == '>' and stack[-1] != '<':
                corrupted = True
                break
            stack.pop()
    if not corrupted:
        incomplete.append(line)

final_scores = []
for line in incomplete:
    stack = []
    for i in range(len(line)):
        if line[i] in ['(', '{', '[', '<']:
            stack.append(line[i])
        elif line[i] in [')', '}', ']', '>']:
            stack.pop()   
    score = 0
    while len(stack):
        score *= 5
        if stack[-1] == '(':
            score += 1 
        elif stack[-1] == '{':
            score += 3
        elif stack[-1] == '[':
            score += 2
        elif stack[-1] == '<':
            score += 4
        stack.pop()
    final_scores.append(score)

final_scores.sort()
print(final_scores[len(final_scores)//2])