polymer = input()
input()
insertions = dict()
while True:
    line = input()
    if line == "":
        break
    first, second = line.split(" -> ")
    insertions[first] = second

for _ in range(10):
    newpolymer = ""
    for i in range(len(polymer)):
        newpolymer += polymer[i]
        if polymer[i:i+2] in insertions:
            newpolymer += insertions[polymer[i:i+2]]
    polymer = newpolymer\

from collections import Counter
count = Counter(polymer)
print(count.most_common()[0][1] - count.most_common()[-1][1])
