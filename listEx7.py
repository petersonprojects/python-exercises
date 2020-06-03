nums = [5,10,15,20,25,30]
length = len(nums)
factor = 5
numsMult = []

for x in range(length):
    numsMult.append(nums[x]*factor)

print(numsMult)