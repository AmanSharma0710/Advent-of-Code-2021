#read list of numbers from terminal
numbers = []

while True:
    num = input()
    if num == "":
        break
    numbers.append(int(num))

ans = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        ans += 1
print(ans)