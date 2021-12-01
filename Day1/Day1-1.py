# load puzzle input
with open("Day1\Depths.txt", "r") as f:
    data = f.readlines()

# convert data type from string to integer
depths = [int(i) for i in data]

counter = 0
# iterate through the depths
for i in range(1, len(depths)):
    # if the current depth was greater than the previous one, add one to the counter
    if depths[i] > depths[i - 1]:
        counter += 1

# output result
print(counter)
