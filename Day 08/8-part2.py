patterns = []

while True:
    line = input()
    if line == "":
        break
    pattern, output = line.split(" | ")
    patterns.append([pattern.split(), output.split()])
answer=0
for pattern in patterns:
    dictionary_number_to_representation = dict()
    for number in pattern[0]:
        if len(number)==2:
            dictionary_number_to_representation[1] = set(number)
        elif len(number)==3:
            dictionary_number_to_representation[7] = set(number)
        elif len(number)==4:
            dictionary_number_to_representation[4] = set(number)
        elif len(number)==7:
            dictionary_number_to_representation[8] = set(number)
    for number in pattern[0]:
        if len(number) == 6:
            curr_num = set(number)
            if len(curr_num.intersection(dictionary_number_to_representation[4])) == 3 and len(curr_num.intersection(dictionary_number_to_representation[1])) == 2:
                dictionary_number_to_representation[0] = curr_num
            if len(curr_num.intersection(dictionary_number_to_representation[4])) == 4:
                dictionary_number_to_representation[9] = curr_num
            if len(curr_num.intersection(dictionary_number_to_representation[1])) == 1:
                dictionary_number_to_representation[6] = curr_num
        if len(number) == 5:
            curr_num = set(number)
            if len(curr_num.intersection(dictionary_number_to_representation[4])) == 2:
                dictionary_number_to_representation[2] = curr_num
            elif len(curr_num.intersection(dictionary_number_to_representation[1])) == 2:
                dictionary_number_to_representation[3] = curr_num
            else:
                dictionary_number_to_representation[5] = curr_num
    output = []
    for output_digit in pattern[1]:
        number = set(output_digit)
        for key, value in dictionary_number_to_representation.items():
            if number == value:
                output.append(key)
                break
    answer += output[0]*1000 + output[1]*100 + output[2]*10 + output[3]

print(answer)
