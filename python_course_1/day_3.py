# Arithmetic Operators (+, -, *, /, %, ** (Exponentiation), // (Floor Division)

number_1 = 2
number_2 = 3

addition = number_1 + number_2
print(addition)

subtraction = number_1 - number_2
print(subtraction)

multiplication = number_1 * number_2
print(multiplication)

division = number_1 / number_2
print(division)

modulus = number_1 % number_2
print(modulus)

exponentiation = number_1 ** number_2
print(exponentiation)

floor_division = number_1 // number_2
print(floor_division)

# ---------------------------------------------------------------
# Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)

number_1 = 2
number_2 = 3

# number_1 = number_1 + number_2
# number_1 += number_2
# number_1 -= number_2
# number_1 *= number_2
# number_1 /= number_2
# number_1 %= number_2
# number_1 **= number_2
number_1 //= number_2
print(number_1)

# ---------------------------------------------------------------
# Comparison Operators (==, !=, <, >, <=, >=)

number_1 = 2
number_2 = 3

# number_3 = number_1 == number_2
# number_3 = number_1 != number_2
# number_3 = number_1 < number_2
# number_3 = number_1 > number_2
# number_3 = number_1 <= number_2
number_3 = number_1 >= number_2
print(number_3)

# ---------------------------------------------------------------
# Logical Operators (and, or, not)

number_1 = 1
number_2 = 1
number_3 = 0

result = number_1 == number_1 and number_1 < number_3
print(result)

result = number_1 == number_1 or number_1 > number_3
print(result)

bool_data = False
print(not bool_data)

# ---------------------------------------------------------------
# Identity Operators (is, is not)

number_1 = 20
number_2 = 20
number_3 = 30

print(number_1 is number_2)
print(number_1 is not number_2)
print(number_1 is not number_3)

# ---------------------------------------------------------------
# Membership Operators (in, not in)

data_arr = [1, 2, 3, 4, 5]
print(1 in data_arr)
print(1 not in data_arr)

# ---------------------------------------------------------------
# Boolean values are either True (1) or False(0)

# Logical Operators (and, or, not)

# True and True = True
# True and False = False
# False and True = False
# False and False = False

# and means multiplication (*)
# 1 * 1 = 1
# 1 * 0 = 0
# 0 * 1 = 0
# 0 * 0 = 0

# print(number_1 < number_2 and number_2 < number_3)

# True or True = True
# True or False = True
# False or True = True
# False or False = False

# ------------------------
# or means addition (+)
# 1 + 1 = 1
# 1 + 0 = 1
# 0 + 1 = 1
# 0 + 0 = 0

number_1 = 2
number_2 = 3
number_3 = 4

print(number_1 < number_2 or number_2 < number_3)
print(number_1 < number_2 or number_2 > number_3)
print(number_2 > number_3 or number_1 < number_2)
print(number_1 > number_2 or number_2 > number_3)

print(not True)


