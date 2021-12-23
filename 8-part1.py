patterns = []

while True:
    line = input()
    if line == "":
        break
    pattern, output = line.split(" | ")
    patterns.append([pattern.split(), output.split()])
answer=0
for pattern in patterns:
    output = pattern[1]
    for digit in output:
        if len(digit) in {2, 3, 4, 7}:
            answer += 1

print(answer)