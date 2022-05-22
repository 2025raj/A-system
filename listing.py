'''
# without using map function
a = [1, 2, 3]
b = [4, 5, 6]
add = a + b # we cann't able to add two list values like this to do so look down; use map function.
print(add)

#result => [1, 2, 3, 4, 5, 6]
'''

# map function
'''
#In list elements:
a = [1, 2, 3]
b = [4, 5, 6]
add = list(map(lambda x, y: x+y, a, b))
print(add)

# result => [5, 7, 9]
'''

# In set elements:
a = {10, 20, 30}  # set
b = {10, 20, 30}
sum_orderway = set(map(lambda x, y: x + y, a, b))
print(sum_orderway)
# run once: logical error
