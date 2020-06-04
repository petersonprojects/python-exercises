
def makeSum():
    numList = [1,2,3,4,5,6,7]
    sum1 = sum(numList)   
    return sum1

def smallest():
    numList = [89,2,17000,105,512,74,7,600]
    numList.sort()
    integer = numList[0]
    return integer

def largest():
    numList = [89,2,17000,105,512,74,7,600]
    numList.sort()
    integer = numList[len(numList)-1]
    return integer




while True:
    query = (int(input("""
                       1. Sum of list
                       2. Largest in list
                       3. Smallest in list
                       Select which functon you want to test >> """)))
    if query == 1:
        result = makeSum()
        print(f'\t\t\t{result}')
    elif query == 2:
        result = smallest()
        print(f'\n\t\t\tLargest number in the list is: {result}')
    elif query == 3:
        result = largest()
        print(f'\n\t\t\tSmallest number in the list is: {result}')
    else:
        break