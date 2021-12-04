# load puzzle input
with open("Day3\BinaryNumbers.txt", "r") as f:
    data = f.readlines()

# remove newline character
binaries = [i.rstrip("\n") for i in data]

# find the gamma and epsilon values
gamma = ""
epsilon = ""
for p in range(len(binaries[0])):
    x = 0
    y = 0
    for i in binaries:

        if i[p] == "0":
            x += 1
        else:
            y += 1
    if x > y:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"


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
gammaD = binaryToDecimal(int(gamma))
epsilonD = binaryToDecimal(int(epsilon))

product = gammaD * epsilonD
print(product)
