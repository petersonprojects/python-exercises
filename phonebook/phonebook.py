#load dictionary data first
import json

with open('phonebook.json', 'r') as filehandler:
    phonebook = json.load(filehandler)

items = phonebook.items()

while True:
    
    print("\nElectronic Phonebook")
    print("========================\n")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")
    
    query = input("\nWhat do you want to do? (1-5): ")
    queryInt = int(query)
    
    if(query == '1'):
        key = input("\nName: ").capitalize()
        print(f'\nFound entry for {key}: {phonebook[key]}')
        
    elif(query == '2'):
        #change/add
        name = input("Name: ").capitalize()
        newNumber = input("Phone# >>")
        phonebook[name]= newNumber
        print(f"Entry stored for {name}")
    elif(query == '3'):
        #delete
        answer = input("Name: ").capitalize()
        del phonebook[answer]
        print(f'Deleted entry for {answer}')
        
    elif(query == '4'):
        #for loop list all entries
        print("")
        for key, value in items:
            print(f'{key}: {value}')
            
    elif(query == '5'):
        #write data to a file
        with open('phonebook.json', 'w') as filehandler:
            json.dump(phonebook, filehandler)
        print("\nPhonebook saved. Program quit.\n")
        break
    
    elif (query == '') or queryInt >= 6:
        print("\n\nInvalid option.\n\t\tTry again.\n")
