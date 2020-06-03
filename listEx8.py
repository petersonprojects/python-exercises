l1 = [2,4,5,16,75]
l2 = [2,3,6,25,0]
length = len(l1)
newList = []

for x in range(length):
    newList.append((l1[x])*(l2[x]))
    
print(newList)