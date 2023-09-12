# Operator Overloading

text_1 = "Hello"
text_2 = " World"

text_3 = text_1 + text_2
print(text_3)

# ---------------------------------------------------------------
# Take input from the user in Python.

number_1 = input("Enter number 1 ")
print(number_1)
print(type(number_1))

number_2 = input("Enter number 2 ")
number_3 = int(number_2)
print(number_3)
print(type(number_3))

# ---------------------------------------------------------------
# Printing output to console.
# In Python, you can use the print() function to display output on the console (terminal).

print("Hello world")

name = "Ram"
surname = "Sharma"
# print("The name is", name)
#
# print("The name is " + name)
#
# print(f"The name is {name}")
# print("The name is {}".format(name))
print("The name is {0} {1}".format(name, surname))

print("Hello", "world", sep="-", end="\n")
print("Hello", "world", sep="-", end="!")

# ---------------------------------------------------------------
# Python data types (classification or categorization of data items).

# Check Data type
# You can use the type() function to check the data type of a variable.

name = "Ram"
number_1 = 10

print(type(name))
print(type(number_1))

# ----------------------
# Numeric Types (int, float, complex)
# integer
# Int or integer is a whole positive or negative number without a decimal point.
# The length of an integer number is unlimited.
# Example: 1,4,5,3,5,100, etc.

# float
# A float is either a positive or a negative decimal point number.
# There is also the possibility of floating numbers with an "e" to indicate a power of 10.
# Example: 100.111, 22.99, 80E2, etc.

# Complex
# Complex numbers are used to represent quantities with both real and imaginary parts.
# It is always written as a numeric value with a "j" text character.
# In this case, the numeric value is the real part, and the number with the character "j" is the imaginary part.
# Example: 2 + 3j, -10j, 5j, etc.
# Complex numbers are used in various mathematical and scientific contexts where quantities have both real and imaginary components.
# Examples: Mathematical Modeling, Signal Processing, Numerical Analysis, Graphics and Visualization, Advanced Mathematics, etc.


number_1 = 1
number_2 = 2.3
number_3 = 1 + 3j

print(number_1)
print(type(number_1))
print(number_2)
print(type(number_2))
print(number_3)
print(type(number_3))

# float number limit after two decimal places in python
number_4 = 2.3333333333

print(round(number_4))
print(format(number_4, ".2f"))
print(float(format(number_4, '.2f')))

# ----------------------
# String Type (Sequence Type Immutable)
# Strings are sequences of characters, and you can access individual characters using indexing and extract substrings using slicing.
# Example: text = "Python" , text[0], text[1], text[1:4]

# text = "Hello World"
text = 'Hello World'

print(id(text))

text = text + " is Good"
print(id(text))

print(text)

print(text.split(" "))

text = 'Hello-World'
print(text.split("-"))

print(text.upper())
print(text.lower())
print(text.replace("World", "Welcome"))

text_2 = 'Welcome'
print(text + " " + text_2)
print("{} {}".format(text, text_2))

print(text[0])
print(text[0:3:1])

print(text == text_2)

text = 'Hello\nWorld'
print(text)

print(len(text))

# ----------------------
# Boolean Type (True(1), False(0))
# In Python, the bool data type represents boolean values, which can have two possible states: True or False.
# Booleans are often used in programming to make decisions and control the flow of a program.
# They are essential for creating conditions, loops, and logic in your code.


value_1 = True
value_2 = False

print(value_1)
print(value_2)
print(not value_2)

number_1 = 10
number_2 = 20

print(number_1 > number_2)


