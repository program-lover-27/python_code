# Python Variables
# In Python, variables are used to store and manage data.
# A variable is a symbolic name that represents a value stored in the computer's memory.
# You can think of a variable as a container for holding different types of data, such as numbers, strings, lists, or more complex objects like functions and classes.
# Variables allow you to manipulate and work with data in your programs.

# Python Naming conventions

name = "Ram"  # allowed
_number = 10  # allowed
number2 = 2.3  # allowed
first_name_2 = "Shyam"  # allowed
firstName = ""
# class = "Python"

print("Hello " + name)
print(_number)
print(first_name_2)
print(number2)

# Python naming conventions not allowed
# any special character in name except _
# Python keyword are not allowed for variable names
# Variable name should not allow start with numeric value (e.g. 2_name)

# Python global and local variables
# A variable outside function are called global variable
# A variable inside a function called the local variable
# To convert local variable to global use 'global' keyword

global course_name
course_name = "Python"  # Global variable


def python_function():
    first_name = "Ram"  # local variable
    print(first_name)

    global last_name  # convert local variable to global
    last_name = "Sharma"


python_function()
print(last_name)

# ---------
# Check variable data types
course_name = "Python"
number_1 = 1
print(type(course_name))
print(type(number_1))
