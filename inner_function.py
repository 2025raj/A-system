# Create an inner function to calculate the addition in the following way:
# 1.Create an outer function that will accept two parameters, a and b.
# Create an inner function inside an outer function that will calculate the addition of a and b.
# At last, an outer function will add 5 into addition and return it.

# question; 2
def outer_function(a, b):
    a = a  # enclosed scope
    b = b

    def inner_function(a, b):

        addition = a + b
        return addition
    addition = inner_function(a, b)

    # addition = addition + 5 or direct method
    return addition + 5


disp = outer_function(10, 20)
print(disp)


#result : 35
