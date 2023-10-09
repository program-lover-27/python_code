# def python_function(*name):
#     print(name)
#
#
# python_function("Ram", "Sharma", "10th", 800, 500)


# def add(*data):
#     sum = 0
#     for num in data:
#         sum = sum + num
#         # print(f"num: {num}, sum: {sum}")
#         # sum = 0 + 1 # 1
#         # sum = 1 + 2 # 2
#     return sum
#
#
# addition = add(2, 3, 4)
# print(addition)


# def python_function(name, surname):
#     print(name)
#     print(surname)
#
#
# python_function(surname="Sharma", name="Ram")


# def python_function(**data):
#     print(data["surname"])
#     print(data["name"])
#     print(data["my_data"])
#
#
# python_function(surname="Sharma", name="Ram", div="10th", marks=800, my_data={"name": "Virat"})


# square = lambda a: a * 2
# print(square(10))

# sum = lambda a, b: a + b
# print(sum(10, 15))


# name = lambda a: a.upper()
# print(name("ram"))
#
# multiply_numbers = lambda a, b : \
#     a * b
#
# print(multiply_numbers(2, 3))

# name = "Hello " \
#        "world"
#
# print(name)


# def my_function(num):
#     if num == 0:
#         print("Function call finish")
#     else:
#         print("Hello world")
#         my_function(num - 1)
#
#
# my_function(2)


# def my_function():
#     def welcome_function():
#         print("Hello world")
#
#     # welcome_function()
#     return welcome_function

# my_function.welcome_function()
# my_function().welcome_function()

# my_function()


# welcome = my_function
# welcome()()
# welcome = my_function
# print(type(welcome))
# welcome()
# welcome_function()


# def my_function():
#     print("Hello world")
#
#
# name = my_function
# name()

# def my_function(func):
#     func()
#
# def welcome():
#     print("Welcome")
#
# my_function(welcome)


# text = "Hello world"
# print(text.upper())


# def upper_text(func):
#     def wrapper():
#         return func().upper()
#
#     return wrapper


# @upper_text
# def say_hello():
#     return "Hello world"
#     # return "Hello world".upper()
#
#
# print(say_hello())


# message = say_hello()
# print(message.upper())
# print(message)


# def add(a, b):
#     return a + b
#
#
# def calculate(func, c, d):
#     return func(c, d)
#
#
# print(calculate(add, 5, 15))




# def upper_text(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
#
#
# @upper_text
# def say_hello():
#     return "Hello world"


# name = upper_text
# print(name(say_hello()))

# print(say_hello())



# def welcome(function):
#     def greet():
#         print("Welcome.")
#         return function()
#     return greet
#
# def say_hello():
#     print("Hello World.")
#
# say_hello()

# text = welcome(say_hello)
# text()
