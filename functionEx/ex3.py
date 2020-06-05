
def shortest(stringList):
    temp = len(stringList[0])
    for val in stringList:
        if(len(val) < temp):
            shortString = val
    return shortString

strings = ["these", "are", "some", "example", "strings", "and", "should", "return", "hi"]
result = shortest(strings)
print(f'Shortest string in the list is: {result}')