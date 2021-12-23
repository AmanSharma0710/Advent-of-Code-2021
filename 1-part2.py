#read list of numbers from terminal
numbers = []

while True:
    num = input()
    if num == "":
        break
    numbers.append(int(num))

ans = 0
last = numbers[0] + numbers[1] + numbers[2]
for i in range(len(numbers)):
    if (i<2):
        continue
    curr = numbers[i-2] + numbers[i-1] + numbers[i]
    if curr > last:
        ans+=1
    last = curr
print(ans)