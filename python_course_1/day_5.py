# Python conditional statements
# If conditional statement
print(2 < 3)

if 2 < 3:
    print("2 is less than 3")

# Nested if conditional statement
if 2 < 3:
    print("2 is less than 3")
    if 2 < 3:
        print("3 is less than 4")

# If - else conditional statement
if 1 > 2:
    print("2 is less than 3")
else:
    print("2 is not less than 3")

# If - elif - else conditional statement
if 1 > 2:
    print("2 is less than 3")
elif 2 > 3:
    print("3 is less than 4")
else:
    print("None of the above.")

# ---------------------------------------------------------------
# Type casting
# It is the process of changing the data type of a value from one type to another in a programming language.
# It's important to note that not all types can be implicitly or explicitly converted to each other.
# For example, trying to convert a string that is not a valid numeric representation to an integer or float will result in an error.

# Implicit Type Conversion:
# Python performs implicit type conversion automatically when different data types are combined in an expression.

number_1 = 2
number_2 = 3.4

number_3 = number_1 + number_2
print(number_3)

# Explicit Type Conversion (Type Casting):
# You can explicitly convert one type to another using built-in functions. The most common type casting functions are:
# int(): Convert to an integer.
# float(): Convert to a float.
# str(): Convert to a string.
# list(): Convert to a list.
# tuple(): Convert to a tuple.

number_1 = 10
number_2 = "10"
number_3 = 10.22

print(int(number_1))
print(int(number_2))
print(int(number_3))

# Using String Formatting:
# String formatting can also be used to perform type casting while embedding variables into strings.

number_4 = 20
text = "The sum is : " + str(number_1 + number_4)
print(text)

# ---------------------------------------------------------------
# Python List Data Type

# In Python, the built-in list data type is often used to represent arrays, which are ordered collections of elements.
# While Python does not have a built-in array type like some other programming languages, the list type can be used effectively to achieve similar functionality.


# Creating Lists (Arrays):
# You can create a list by enclosing comma-separated elements within square brackets [].
numbers = [1, 2, 3, 4, 5]
names = ["Ram", "Shyam", "Mohan"]

print(numbers)
print(names)

# A List Allows Duplicate Items:
numbers = [1, 1, 2, 2, 3]
print(numbers)

# Python List Items Data Types
# There is no restriction on adding similar data type items into the list, you can add different data types as well.
list1 = [0, 1, 2]
list2 = ["Red", "Blue", "Green"]
list3 = [True, False, True]
list4 = [1, "Red", True]

print(list1)
print(list2)
print(list3)
print(list4)

# Python list() Constructor
# You can also create a list using the list() constructor.
numbers_list = list((0, 1, 2, 3, 4, 5))

print(numbers_list)

# List Items Count
# To determine how many items are in the list, use the len() function.
numbers_list = [0, 1, 2, 3, 4, 5]
print(len(numbers_list))

# Access List Items
# The list items are indexed.
# The first item of the list index position is 0.
# You can access list items by using the index position with square brackets ([]).
colors_list = ["Red", "Blue", "Green"]
print(colors_list[1])

# When you use negative indexing in Python, item picking starts from the end of the list.
# You can access items from the end, meaning that if you put index [-1], you get the last item from the list, and if you put index [-2], you get the second-last item from the list.
colors_list = ["Red", "Blue", "Green"]
print(colors_list[-1])

# Range of Indexes
# Range of Indexes is also called Slicing.
# List slicing means taking some part from the original list.
# To slice the list, we provide the start item index position, end item index position, and step count separated by a colon.
colors_list = ["Red", "Blue", "Green", "Orange", "White", "Black", "Yellow"]
print(colors_list[1:5])

# Range of Indexes Specifies Only the Start Position
# In the slicing, when you specify where to start and ignore the end item position, automatically it goes to the end of the list.
colors_list = ["Red", "Blue", "Green", "Orange", "White", "Black", "Yellow"]
print(colors_list[3:])

# Range of Indexes Specifies Only the End Position
# In the slicing, when you ignore where to start and specify only the end item position, the indexes will begin from the first item and goes up to the specified index position.
colors_list = ["Red", "Blue", "Green", "Orange", "White", "Black", "Yellow"]
print(colors_list[:4])

# Range of Negative Index
# In the slicing with negative indexes, you can specify where to start and where to end (negative indexing starts picking items from the end), and when you do that, it returns a new list with items between the start and end indexes.
colors_list = ["Red", "Blue", "Green", "Orange", "White", "Black", "Yellow"]
print(colors_list[-5:-2])

# Check item exists in the list
# Check if the specified item exists in the list by using the "in" keyword.
colors_list = ["Red", "Blue", "Green"]
if "Blue" in colors_list:
    print("Blue exists in the list.")
else:
    print("Blue does not exist in the list.")
