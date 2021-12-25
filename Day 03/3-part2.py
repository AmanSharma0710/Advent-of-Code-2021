numbers_in_binary = []


while True:
    number = input()
    if number == "":
        break
    numbers_in_binary.append(number)

oxygen_rating = ""
o2_list = numbers_in_binary.copy()

for position in range(len(numbers_in_binary[0])):
    if(len(o2_list)==1):
        oxygen_rating = o2_list[0]
        break
    new_ls = []
    ones = 0
    zeros = 0
    for number in o2_list:
        if(number[position]=='1'):
            ones+=1
        else:
            zeros+=1
    common = ''
    if ones >=zeros:
        common += '1'
    else: 
        common += '0'
    for number in o2_list:
        if number[position] == common[0]:
            new_ls.append(number)
    o2_list = new_ls.copy()
    new_ls.clear()
if(len(o2_list)==1):
    oxygen_rating = o2_list[0]
    
carbon_rating = ""
co2_list = numbers_in_binary.copy()

for position in range(len(numbers_in_binary[0])):
    if(len(co2_list)==1):
        carbon_rating = co2_list[0]
        break
    new_ls = []
    ones = 0
    zeros = 0
    for number in co2_list:
        if(number[position]=='1'):
            ones+=1
        else:
            zeros+=1
    common = ""
    if ones >=zeros:
        common = '0'
    else: 
        common = '1'
    for number in co2_list:
        if number[position] == common[0]:
            new_ls.append(number)
    co2_list = new_ls.copy()
    new_ls.clear()
if(len(co2_list)==1):
    carbon_rating = co2_list[0]

o2_rating_decimal = int(oxygen_rating, 2)
co2_rating_decimal = int(carbon_rating, 2)

print(o2_rating_decimal*co2_rating_decimal)