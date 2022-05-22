'''
16. Accept string from the user and display only those characters which are 
present at an odd index.

'''
# solution:

string_value = input("enter your name: ")
# string_value = "rajoli"
for i in string_value[0::2]:
    print(f"Chars of a string in odd index/position is:  {i}")

# output => r, j, l
