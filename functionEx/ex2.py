def largest(numList):
    numList.sort()
    length = len(numList)
    return numList[length-1]

numberList = [-2000, 5 , 10, -15000 , 20, 25, 30]

result = largest(numberList)

print(f'Largest number in the list is: {result}')