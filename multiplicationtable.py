#que: 10

''' Write a program that prompts the user to input a positive integer. It should then print the multiplication 
    table of that number. '''


def multi_table(num):
    for i in range(1, 11):
        multi = num * i
        print(f"{num} * {i} = {multi}")


num1 = int(input("enter a only positive number"))
if num1 > 0:
    multi_table(num1)
else:
    print("please re-enter your wished positive value ")


# To get the result of this run the program.
