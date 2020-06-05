
# file_handler = open('hello.txt','w')

# file_handler.write('''Hello World
#                     this
#                     is more
#                     example
#                     text
#                    ''')

# file_handler.close()

# file_handler = open('sample.html', 'r')

# contents = file_handler.read()

# file_handler.close()

# print(contents)

import pickle

# data = {"name": 'Paul'}

# with open('data.pickle', 'wb') as filehandler:
#     pickle.dump(data, filehandler)

with open('data.pickle', 'rb') as filehandler:
    data = pickle.load(filehandler)
    print(data["name"])
