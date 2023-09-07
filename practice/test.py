N = 5
list = [0] * N
list_comprehension = [0 for _ in range(N)]
rows, cols = (5, 5)
twod_list = [[0]*cols]*rows
twod_list_comprehension = [[0 for _ in range(cols)] for _ in range(rows)]
print(list)
print(list_comprehension)
print(twod_list)
print(twod_list_comprehension)
twod_list[0][0] = 100
twod_list_comprehension[0][0] = 1000
print(twod_list)
print(twod_list_comprehension)

list_from_loop = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)

    list_from_loop.append(row)
print(list_from_loop)

# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)



my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # output: ['banana', 'cherry']

fruits = ['apple', 'banana', 'cherry', 'guava', 'grapes', 'mango', 'orange']
print(fruits[3:])

palindrome = ['malayalama']


i = 0
j = len(palindrome)-1
if palindrome[0:j+1] == palindrome[0][::-1]:
    print("its palindrome")
else:
    print("its not palindrome")

print(palindrome[i:j+1])
print(palindrome[i][::-1])

x = 'sameer'
print(x)
print(x[::-1])

import math 
print(math.inf)

print(pow(2,31)-1)
print(-pow(2,31))

