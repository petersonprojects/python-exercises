def longest(stringList):
    temp = len(stringList[0])
    for val in stringList:
        if(len(val) > temp):
            longString = val
    return longString

strings = ["these", "are", "some", "example", "strings", "and","it", "should", "return", "oogabooga"]
result = longest(strings)
print(f'Longest string in the list is: {result}')