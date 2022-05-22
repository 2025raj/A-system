
# 1. create a function using variable length arguments.

# we are passing variable length arguments into the function:
def addition(*x):  # (*) denotes variable length arguments.
    z = x[0] + x[1] + x[2]   # indexing matters the most and :.z = 10 + 30
    print(z)  # hide values which are not indexed.


# (Indexing starts from 0 like Index(0) = 10, 1 = 20, 2 = 30)
addition(10, 20, 30)

# point to be remember : we can pass different number of arguments in one variable in both variable length arguments and keyword variable length varguments.

# result = 10 + 30 => 40...
