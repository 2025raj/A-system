'''
19. Write a Python program to print the odd numbers from a given list. 
Sample List : [12,13,14,15,16,17,18,19]

'''
# solution:
sample_list = [12, 13, 14, 15, 16, 17, 18, 19]
for i in sample_list:
    if i % 2 == 1:
        print(f"odd num in the given list is: {i}")

'''
output:
odd num in the given list is: 13
odd num in the given list is: 15
odd num in the given list is: 17
odd num in the given list is: 19

'''
