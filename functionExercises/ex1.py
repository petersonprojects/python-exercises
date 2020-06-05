

def smallest(numList):
    numList.sort()
    return numList[0]

numberList = [-2000, 5 , 10, -15000 , 20, 25, 30]

result = smallest(numberList)

print(f'Smallest number in the list is: {result}')