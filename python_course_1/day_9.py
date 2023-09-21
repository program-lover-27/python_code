# li = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
#
# length = len(li)
# for i in range(0, length):
#     for j in range(i):
#         if li[i] < li[j]:
#             temp = li[i]
#             li[i] = li[j]
#             li[j] = temp
#
# print(li)


# data_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def reverse_list(data_arr, start):
#     return reverse_list[start]


# -------------------------------------------------------
# Python Dictionary


# data_arr = ("key1", "key2", "key3")
#
# map_dict = dict.fromkeys(data_arr, 0)
#
# print(map_dict)

# obj = map(lambda a: a * a, 1)
# for i in obj:
#     print(i)


colors_set = {"Red", "Blue", "Green"}


# colors_set.remove("Blue")
# colors_set.discard("Blue")
# colors_set.pop()
# colors_set.pop(1)
# colors_set.clear()
# del colors_set
# print(colors_set)

# company_dictionary = {}
#
# # print(type(company_dictionary))
# company_dictionary["name"] = "Google"
#
# print(type(company_dictionary))
# print(company_dictionary)

# company_dictionary = {
#     "name": "Google",
#     "country": "USA",
#     "start_year": 1995
# }

# company_name = company_dictionary.keys()
# company_name = company_dictionary.values()
# company_name = company_dictionary.items()
# print(company_name)


# if "Google" in company_dictionary.values():
#     print("There is a Google value in the dictionary.")
# else:
#     print("There is no Google value in the dictionary.")

# if "name" in company_dictionary:
#     print("There is a name key in the dictionary.")
# else:
#     print("There is no name key in the dictionary.")

#
# for key, value in company_dictionary.items():
#     # print(company_dictionary[key])
#     # print(f"key: {key},     value: {company_dictionary[key]}")
#     print(f"key: {key},     value: {value}")


# print(len(company_dictionary))
#
# # company_dictionary["name"] = "Alphabet"
# company_dictionary["parent_company"] = "Alphabet"
#
# print(company_dictionary)
# print(len(company_dictionary))


# company_dictionary.update({"name": "Alphabet"})
# company_dictionary.update({"parent_company": "Alphabet"})
#
# print(company_dictionary)


#
# number = 10
# del number
# print(number)


# print(company_dictionary[1])

# company_dictionary.pop("start_year")
# del company_dictionary["start_year"]
#
# print(type(company_dictionary))

# del company_dictionary
# print(company_dictionary)

# number = int(100)
# print(type(number))

# data_dict = dict({"name": "Google"})

# print(data_dict)


# company_dictionary = {
#     "name": "Google",
#     "country": "USA",
#     "start_year": 1995
# }

# company_dictionary.popitem()
# company_dictionary.remove()

# del company_dictionary

# company_dictionary.clear()
#
# print(company_dictionary)


# -------------------------------------------------------

# Python Function


# Argument and parameter


def python_function(name):
    # print(1, name)
    # return "Hello "
    return "Hello " + name


retuned_name = python_function("Rajshri")

print(retuned_name)
