# load puzzle input
with open("Day1\Depths.txt", "r") as f:
    data = f.readlines()

# convert data type from string to integer
depths = [int(i) for i in data]

counter = 0
# iterate through the depths
for i in range(3, len(depths)):
    # current sliding window sum
    currentSum = sum(depths[i - 3:i])
    # previous sliding window sum
    previousSum = sum(depths[i - 4:i - 1])
    # if the current sum was greater than the previous sum, add one to the counter
    if currentSum > previousSum:
        counter += 1

# output result
print(counter)
