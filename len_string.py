'''
12. Write a python program that return the number of characters in a string. 
myList = "Parameter"

'''
# solution 1:
'''
#using Lambda function : cause it holds one epression and it is used to perform single task.
str_length = lambda mylist : len(mylist) 
a = str_length ("parameter")
print(a)
'''
# solution 2:

# using normal function:

# 1. using given value:
'''
def str_length(mylist):
    return len(mylist)


a = str_length("parameter")
print(a)
'''

# 2. user approach:


def str_length(mylist):
    return len(mylist)


b = input("enter a string to find it's length: ")
a = str_length(b)
print(a)
