# question 11

'''
11. Write a program that prompts the user to input an integer and then outputs the
number with the digits reversed. For example, if the input is 12345, the output should
be 54321.

'''


# answer: by doing string slicing.

num = int(input("enter a number"))
str_num = str(num)

for i in str_num[-1:: -1]:

    integer_i = int(i)

    print(integer_i, end="")


# print(type(integer_i)) :: to check final reversed value type....
