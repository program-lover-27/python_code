# Change List Item Value
# In Python, you can change the value of an item in a list by using its index number.
colors_list = ["Red", "Blue", "Green"]
colors_list[1] = "Purple"
print(colors_list)

# Change List Item Values Using Slicing
# You can change specific items from the list using the slicing, define a new list with items and assign that new list to the original list with the index number.
colors_list = ["Red", "Blue", "Green", "Orange", "White"]
new_colors_list = ["Purple", "Grey"]
colors_list[2:4] = new_colors_list
print(colors_list)

# Delete a Slice From the List
# You can also delete items slice from the list using the del keyword.
colors_list = ["Red", "Blue", "Green"]
del colors_list[1:3]
print(colors_list)

# Add At Beginning
# To add a new list at the beginning of the original list, set the end item index to 0 (the list index count starts at 0).
colors_list = ["Red", "Blue", "Green"]
new_colors_list = ["Purple", "Grey"]
colors_list[:0] = new_colors_list
print(colors_list)

# Add At End
# Set the start index count as the length of the original list when adding a new list at the end.
colors_list = ["Red", "Blue", "Green"]
new_colors_list = ["Purple", "Grey"]
colors_list[len(colors_list):] = new_colors_list

# Add In Middle
# To add a new list at the centre of the original list, set the start and end item positions.
colors_list = ["Red", "Blue", "Green"]
new_colors_list = ["Purple", "Grey"]
colors_list[1:1] = new_colors_list
print(colors_list)

# Delete List Item Values Using Range
# If you insert fewer items than specific replace items, then after the new items insert into the specified item positions and remaining items move accordingly.
colors_list = ["Red", "Blue", "Green"]
new_colors_list = ["Purple"]
colors_list[1:3] = new_colors_list
print(colors_list)

# ---------------------------------------------------------------
# Add List Items
# Use the append() function to add a new item to the list.
# When using the append() function, the new item adds at the end of the list.
colors_list = ["Red", "Blue", "Green"]
colors_list.append("Purple")
print(colors_list)

# Add List Items Using Insert Function
# Using the insert() function, you can add a new item at a specified position without removing any other items from the list.
colors_list = ["Red", "Blue", "Green"]
colors_list.insert(2, "Purple")
print(colors_list)

# Extend List
# Use the extend() function to add a new list to the current list.
colors_list = ["Red", "Blue", "Green"]
new_colors_list = ["Purple", "Grey"]
colors_list.extend(new_colors_list)
print(colors_list)

# Remove Specific List Item
# Use the remove() function to remove a specific item from the list.
colors_list = ["Red", "Blue", "Green"]
colors_list.remove("Blue")
print(colors_list)

# Remove Specific List Index
# Use the pop() function to remove a specific index from the list.
# When you do not specify the index position in pop(), it will remove the last item from the list.
colors_list = ["Red", "Blue", "Green"]
colors_list.pop(1)
colors_list.pop()
print(colors_list)

# Remove Specific List Index Using del keyword.
# Use the del keyword to remove a specific index from the list.
colors_list = ["Red", "Blue", "Green"]
del colors_list[0]
print(colors_list)

# Delete entire list
# Use the del keyword to delete the entire list.
colors_list = ["Red", "Blue", "Green"]
del colors_list
# print(colors_list)

# Delete all items from the list
# Use the clear() function to empty the list. It will delete all items from the list, but the list will still exist.
colors_list = ["Red", "Blue", "Green"]
colors_list.clear()
print(colors_list)

# ---------------------------------------------------------------



# # break, continue, pass
#
# def my_function():
#     print("Hello world")
#
#
# my_function()
# # for number in range(1, 5):
# #
# #     if number == 2:
# #
# #     print(number)
# # else:
# #     print("For loop completed")
#
# # number_list = list((1, 2, 3, 4, 5))
#
#
# # number_list.remove(2)
# # number_list.pop(2)
#
# # number_list.clear()
# # print(id(number_list))
# # del number_list
# # print(id(number_list))
# # print(number_list)
#
# # number_list.append(10)
# # number_list.insert(1, 10)
# # number_list[1:1] = [10]
# # number_list[0:len(number_list):1] = [10]
# number_list[0::1]
#
# # number_list_2 = [10, 15, 20]
# # number_list.append(number_list_2)
#
# # number_list[:0] = [10, 11, 12]
# # number_list[len(number_list):] = [10, 11, 12]
# # number_list[4:5] = [10, 11, 12]
# # print(number_list)
#
#
# # number_list[0:len(number_list): 1]
# # del number_list[0:2:]
# # print(number_list)
#
#
# # print(type(number_list))
# # print(len(number_list))
#
# # print(number_list[:3:])
#
# # if 10 in number_list:
# #     print("Exist")
# # else:
# #     print("Not exist")
