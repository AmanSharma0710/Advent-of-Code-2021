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
    return packet, length

def process_operator(packet):
    version = int(packet[0:3], 2)
    global totalversion
    totalversion += version
    typeid = int(packet[3:6], 2)
    packet = packet[6:]

    totalLength = 6
    if typeid == 4:
        packet, length = process_literal(packet)
        totalLength += length
        return packet, totalLength
    lengthtype = int(packet[0])
    totalLength += 1
    packet = packet[1:]
    if lengthtype == 1:
        numberOfSubpackets = int(packet[0:11], 2)
        totalLength += 11
        packet = packet[11:]
        for i in range(numberOfSubpackets):
            packet, length = process_operator(packet)
            totalLength += length
        return packet, totalLength
    elif lengthtype == 0:
        lengthOfSubpackets = int(packet[0:15], 2)
        totalLength += 15
        packet = packet[15:]
        while lengthOfSubpackets > 0:
            packet, length = process_operator(packet)
            lengthOfSubpackets -= length
            totalLength += length
        return packet, totalLength
    
process_operator(transmission)
print(totalversion)