'''15. Accept string from the user and display only those characters which are 
present at an even index.
'''

# answer:

# algorithm section:
'''
take a input as string datatype from the user.
diplay char of given string which are at even index/position.

'''

string_value = input("enter your name: ")
# taking refernce from a value or a string called
# assuming: string_value = "rajoli"
for i in string_value[1::2]:
    print(f"chars of string at even index is {i}")


#result = a, o, i
