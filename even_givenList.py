'''
18. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

# solution:
# using filter function: value comes in sequence..(look output like 2, 4, 6, 8)
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number = list(filter(lambda x: x % 2 == 0, sample_list))
print(f"even numbers in a given list are: {even_number}")


'''
output:

even numbers in a given list are: [2, 4, 6, 8]

'''
