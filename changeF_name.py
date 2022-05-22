'''3.Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_tudent(name, age)
to it and call it using the new name.'''


def display_student(name, age):
    print(name, age)

    # once call using original name
    # display_student("Emma", 26)


# assign new name
# generally changing the name of function before calling it.
show_student = display_student
# call using new name
show_student("babu", 5)
