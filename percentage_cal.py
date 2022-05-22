'''
20. Write a program to accept percentage and display the Category according to the  following criteria :
Percentage	Category
< 41	                     Failed
>=41 & <55	Fair
>=55 & <65	Good
>=65	                     Excellent

'''

# solution:

percentage = float(input("enter your percentage "))
if percentage >= 0 and percentage <= 100:
    if percentage >= 65:
        print("excellent")
    elif percentage >= 55 and percentage < 65:
        print("good")
    elif percentage >= 41 and percentage < 55:
        print("fair")
    else:
        print("failed")

else:
    print("invalid: enter a correct number between 0 to 100 ")
