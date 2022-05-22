'''
13. Write a Python program to multiply all the numbers in a list using while and for loop.
Sample list = [8,2,3,-1,7]

'''


# answer:1

# by using for loop:

# followed algorithm:
'''
sample_list = [8, 2, 3, -1, 7]
i = sample_list[0]
j = sample_list[1]
k = sample_list[2]
l = sample_list[3]
m = sample_list[4]
multi = i * j * k * l * m
print(multi)
'''


sample_list = [8, 2, 3, -1, 7]
multi = 1
for i in range(0, 5):
    multi = multi * sample_list[i]
print(
    f"the multiple of all elements which are given in the sample_list is {multi} ")


# answer:2
# using while loop
sample_list = [8, 2, 3, -1, 7]
i = 0
multi = 1
while i < 5:  # 5 == length of list (len(sample_list))
    multi = multi * sample_list[i]  # list indexing
    i = i + 1
print(multi)
