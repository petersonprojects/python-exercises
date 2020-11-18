
# 2520 is the smallest number that can be divided by each 
# of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

count = 0

for number in range(20,300000000):
    for divide in range(1,21):
        if(number%divide == 0):
            count+=1
            if(count >= 20):
                print(number)
    count = 0





