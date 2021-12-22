numbers_in_binary = []
gamma = ""
epsilon = ""


while True:
    number = input()
    if number == "":
        break
    numbers_in_binary.append(number)

for position in range(len(numbers_in_binary[0])):
    ones = 0
    zeros = 0
    for number in numbers_in_binary:
        if number[position] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)
print(gamma_decimal*epsilon_decimal)
    