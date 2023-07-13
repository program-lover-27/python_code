import copy as cp

numbers_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# Deep copy
copy_numbers_list = cp.deepcopy(numbers_list)

print(numbers_list)
print(copy_numbers_list)

print("Original and copy object ids")
print(id(numbers_list))
print(id(copy_numbers_list))

print("Original and copy nested object ids")
print(id(numbers_list[0]))
print(id(copy_numbers_list[0]))

numbers_list[0][0] = "AA"

print(numbers_list)
print(copy_numbers_list)
