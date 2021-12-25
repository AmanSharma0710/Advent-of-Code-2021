square = 0
triangle = 0
curly = 0
round = 0
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
    if corrupted:
        if line[i] == ')':
            round += 1
        elif line[i] == '}':
            curly += 1
        elif line[i] == ']':
            square += 1
        elif line[i] == '>':
            triangle += 1

print(round*3 + square*57 + curly*1197 + triangle*25137)
    