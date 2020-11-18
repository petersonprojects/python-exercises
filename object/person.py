class Person: 
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = 0
    
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))
        self.count += 1
        
    def print_info(self):
        print(f'Email: {self.email}\nPhone#: {self.phone}')
        
    def add_friend(self, name):
        self.friends.append(name)
        
    def num_friends(self):
        return len(self.friends)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet("Jordan")
jordan.greet("Sonny")

sonny.print_info()
sonny.add_friend("Micah")
print(sonny.num_friends())



# class Button:
#     def __init__(self):
#         self.count = 0
        
#     def click(self):
#         self.count += 1
        
#         if self.count > 2:
#             print("Need some help there bud?")
#             self.count = 0
            
# navButton = Button()
# helpButton = Button()

# print(navButton.count)
# navButton.click()
# helpButton.click()
# print(navButton.count)
# navButton.click()
# print(navButton.count)
# navButton.click()
# helpButton.click()
# print(navButton.count)
# navButton.click()
# helpButton.click()

# print(f'Nav: {navButton.count}')
# print(f'Help: {helpButton.count}')

# class SString(str):
    
#     def reverse(self, name):
#         rstring = ""
        
#         for char in name:
#             rstring = char + rstring
            
#         return rstring
    
# myString = SString("hello")

# print(myString.reverse("hello"))