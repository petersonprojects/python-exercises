a = [ [1,3], [2,4], [69,70]]
b = [ [5,2], [1,0], [100,45] ]

i_index = 0
o_index = 0

while o_index < len(a):
    while i_index < len(a[o_index]):
        newNum = a[o_index][i_index] + b[o_index][i_index]
        print(f'{newNum}')
        i_index += 1
    i_index = 0
    o_index += 1