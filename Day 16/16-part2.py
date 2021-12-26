#parse the input
hextransmission = input()
hextransmission = hextransmission.lower()
hextransmission = list(hextransmission)
transmission = ""
for i in hextransmission:
    decimal = int(i, 16)
    binary = bin(decimal)[2:]
    binary = "0" * (4 - len(binary)) + binary
    transmission += binary

totalversion = 0

#if type id is 4, it is literal value
#otherwise it is operator packet

#structure of packet:
#version, typeid, everything else

#function that carries out processing of a literal value and returns the literal value
def process_literal(packet):
    number = ""
    length = 0
    while True:
        length += 5
        chunk = packet[0:5]
        number += chunk[1:]
        packet = packet[5:]
        if chunk[0] == "0":
            break
    return packet, length, int(number, 2)

#recursively processes an operator packet and returns the final value
def process_operator(packet):
    version = int(packet[0:3], 2)
    global totalversion
    totalversion += version
    typeid = int(packet[3:6], 2)
    packet = packet[6:]
    totalLength = 6
    if typeid == 4:
        packet, length, value = process_literal(packet)
        totalLength += length
        return packet, totalLength, value
    sum = 0
    product = 1
    minimum = float("inf")
    maximum = float("-inf")
    lengthtype = int(packet[0])
    totalLength += 1
    packet = packet[1:]
    if lengthtype == 1:
        numberOfSubpackets = int(packet[0:11], 2)
        totalLength += 11
        packet = packet[11:]
        for i in range(numberOfSubpackets):
            packet, length, value = process_operator(packet)
            totalLength += length
            sum += value
            product *= value
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
            if i==0:
                a = value
            if i==1:
                b = value
    elif lengthtype == 0:
        lengthOfSubpackets = int(packet[0:15], 2)
        totalLength += 15
        packet = packet[15:]
        first = True
        second = True
        while lengthOfSubpackets > 0:
            packet, length, value = process_operator(packet)
            lengthOfSubpackets -= length
            totalLength += length
            sum += value
            product *= value
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
            if first:
                a = value
                first = False
                continue
            if second:
                b = value
                second = False
    if typeid == 3:
        return packet, totalLength, maximum
    elif typeid == 2:
        return packet, totalLength, minimum
    elif typeid == 1:
        return packet, totalLength, product
    elif typeid == 0:
        return packet, totalLength, sum
    elif typeid == 5:
        return packet, totalLength, int(a>b)
    elif typeid == 6:
        return packet, totalLength, int(a<b)
    elif typeid == 7:
        return packet, totalLength, int(a==b)
    return float("inf")

transmission, length, value= process_operator(transmission)
print(value)