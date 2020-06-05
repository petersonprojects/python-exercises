answer = ''
coins = 0
print(f"You have {coins} coins.")

while (answer != 'no'):
    answer = input("Do you want another? ")
    answer = answer.lower()
    
    if answer == 'yes':
        coins = coins + 1
        print(f"You have {coins} coin(s).")
    elif answer != 'no':
        print('Try again.')
        
print("Bye")