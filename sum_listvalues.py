'''
14. Write a Python program to sum all the numbers in a list using for loop and while loop.
Sample list : [8, 2, 3, 0, 7]
'''


# algorithm
'''
a = sample_list[0]
b = sample_list[1]
c = sample_list[2]
d = sample_list[3]
e = sample_list[4]
sum = a + b + c + d + e
print(sum)
'''


# using for loop:
sample_list = [8, 2, 3, 0, 7]
sum = 0
for i in range(0, 5):
    sum = sum + sample_list[i]
    # print(sum)

print(f"the sum of all elements which are in the list is {sum}")


# using while loop:

sample_list = [8, 2, 3, 0, 7]
i = 0
sum = 0
while i < 5:
    sum = sum + sample_list[i]  # list indexing #modifying sum
    i = i + 1
print(f"the sum of all values which are in the list is {sum}")
