# load puzzle input
with open("Day3\BinaryNumbers.txt", "r") as f:
    data = f.readlines()

# remove newline character
binaries = [i.rstrip("\n") for i in data]

# find the oxygen generator rating
trimmed = binaries
for p in range(len(binaries[0])):
    x = 0
    y = 0
    # determine the most common number
    for i in trimmed:

        if i[p] == "0":
            x += 1
        else:
            y += 1
    if x > y:
        trimmed = [i for i in trimmed if i[p] == "0"]
    else:
        trimmed = [i for i in trimmed if i[p] == "1"]
    if len(trimmed) == 1:
        break

oxygen = trimmed[0]

# find the CO2 scrubber rating
trimmed = binaries
for p in range(len(binaries[0])):
    x = 0
    y = 0
    # determine the most common number
    for i in trimmed:

        if i[p] == "0":
            x += 1
        else:
            y += 1
    if x > y:
        trimmed = [i for i in trimmed if i[p] == "1"]
    else:
        trimmed = [i for i in trimmed if i[p] == "0"]
    if len(trimmed) == 1:
        break
CO2 = trimmed[0]


# binary to decimal converter
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal


# convert binary values to decimal
oxygenD = binaryToDecimal(int(oxygen))
CO2D = binaryToDecimal(int(CO2))

product = oxygenD * CO2D
print(product)
