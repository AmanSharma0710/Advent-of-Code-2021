template = input()
input()
insertions = dict()
while True:
    line = input()
    if line == "":
        break
    first, second = line.split(" -> ")
    insertions[first] = second
from collections import defaultdict
polymer = defaultdict(int)
for i in range(len(template)-1):
    polymer[template[i:i+2]] += 1

for _ in range(40):
    newpolymer = defaultdict(int)
    for key, value in polymer.items():
        if key in insertions:
            newpolymer[key[0] + insertions[key]] += value
            newpolymer[insertions[key] + key[1]] += value
        else:
            newpolymer[key] += value
    polymer = newpolymer
count = defaultdict(int)
for key, value in polymer.items():
    count[key[0]] += value
    count[key[1]] += value
count[template[-1]] += 1
count[template[0]] += 1
for key, value in count.items():
    count[key] //= 2
values = list(count.values())
values.sort()
print(values[-1] - values[0])