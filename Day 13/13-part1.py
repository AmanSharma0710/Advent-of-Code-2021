dots = set()
while True:
    line = input()
    if line == "":
        break
    x, y = line.split(",")
    dots.add((int(x), int(y)))

line = input().split(" ")
fold = line[2]
axis, value = fold.split("=")
value = int(value)
tobedeleted = set()
tobeadded = set()
for dot in dots:
    if axis == "x":
        if dot[0] > value:
            x, y = dot
            tobedeleted.add((x, y))
            tobeadded.add((2*value - x, y))
    elif axis == "y":
        if dot[1] > value:
            x, y = dot
            tobedeleted.add((x, y))
            tobeadded.add((x, 2*value - y))
for dot in tobedeleted:
    dots.remove(dot)
for dot in tobeadded:
    dots.add(dot)
print(len(dots))


