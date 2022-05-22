# question no.9


'''Write a function for checking the speed of drivers. 
If speed is less than 70, it should print “Ok”.
if the speed is 80, it should print: “Warning”.'''


# answer:
def speed_test(speed):
    if speed < 70:
        print("ok")
    elif speed > 80:
        print("warning")


a = int(input("enter a num "))
speed_test(a)
