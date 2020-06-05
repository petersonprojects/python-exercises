bill = float(input("Bill amount >>> "))
service = input("Level of service (good, fair or bad)>>> ")

if service == "good":
    tipAmt = bill*0.2
    print(f'Tip Amount: ${tipAmt}')
    total = bill + tipAmt
    rounded = round(total,2)
    print(f'Total amount: ${rounded})')

if service == "fair":
    tipAmt = bill*0.15
    print(f'Tip Amount: ${tipAmt}')
    total = bill + tipAmt
    rounded = round(total,2)
    print(f'Total amount: ${rounded}')
    
if service == "bad":
    tipAmt = bill*0.1
    print(f'Tip Amount: ${tipAmt}')
    total = bill + tipAmt
    rounded = round(total,2)
    print(f'Total amount: ${rounded}')