#load dictionary data and json module
import json

def load():
    with open('phonebook.json', 'r') as filehandler:
        phonebook = json.load(filehandler)
    return phonebook

def lookUp():
    while True:
        key = input("\nName: ").capitalize()
        isFound = key in phonebook
        
        if(isFound):
            print(f'\nFound entry for {key}: {phonebook[key]}')
            break
        else:
            print('Not found. Try again.')

def setEntry():
    name = input("Name: ").capitalize()
    newNumber = input("Phone# >>")
    
    phonebook[name] = newNumber
    
    print(f"Entry stored for {name}")
    
def listAllEntries():
    items = phonebook.items()
    print("")

    for key, value in items:
        print(f'{key}: {value}')

def deleteEntry():
            #delete
    while True:
        answer = input("Name to delete: ").capitalize()
        
        isFound = answer in phonebook
        
        if(isFound):
            del phonebook[answer]
            print(f'Deleted entry for {answer}')
            break
        else:
            print("Name not found. Try again.")
            
def saveData():
    with open('phonebook.json', 'w') as filehandler:
        json.dump(phonebook, filehandler)
    print("\nPhonebook saved. Program quit.\n")
    
def default():
    print("\n\nInvalid option.\n\t\tTry again.\n")

phonebook = load()

while True:
    
    print("""
                Electronic Phonebook
                ========================
                1. Look up an entry
                2. Set an entry
                3. Delete an entry
                4. List all entries
                5. Quit 
            
            """)
    
    query = input("\nWhat do you want to do? (1-5): ")
    
    if(query == '1'):
        
        lookUp()

    elif(query == '2'):
        
        setEntry()
        
    elif(query == '3'):
        
        deleteEntry()

    elif(query == '4'):
        
        listAllEntries()

    elif(query == '5'):
        
        saveData()
        break
    
    else:
        default()

