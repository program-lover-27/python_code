# def welcome(name):
#     print(name)
#
# welcome("John")
#
# hello = welcome
# hello("John")


# def double(number):
#     return number * number
#
# def half(number):
#     return number / 2
#
# def get_number(function, number):
#     result = function(number)
#     return result
#
# print(get_number(double, 2))
# print(get_number(half, 2))

# def welcome():
#     def greet():
#         print("Welcome.")
#
#     return greet
#
#
# text = welcome()
# text()

# text = welcome()()
# text


# def welcome(abc):
#     def greet():
#         print("Welcome.")
#         return abc()
#
#     return greet
#
#
# def say_hello():
#     print("Hello World.")


# say_hello()

# text = welcome(say_hello)
# text()


# def capital_text_decorator(function):
#     def wrapper():
#         print("Welcome")
#         text = function()
#         return text.upper()
#
#     return wrapper
#
# def capital_text_decorator1(function):
#     def wrapper():
#         text = function()
#         print("Hello")
#         return text.lower()
#
#     return wrapper
#
#
# @capital_text_decorator1
# @capital_text_decorator


# def say_hello():
#     return "Hello john"
#
#
# print(say_hello())


# class Person:
#
#     def display(self):
#         print(self)
#
#     def display_name(abc, name):
#         print(abc)
#
#
# obj = Person()
# print(obj)
#
# obj.display()
# obj.display_name("Ram")


# def main():
#     print("Main function")
#
# main()


# def display(**data):
#     print(data)
#
# display(name="Ram")


# class Man:
#
#     def display(xyz, name, surname):
#         print("Hello", name, surname)
#
#
# abc = Man()
# abc.display("Ram", "Sharma")
# print(abc)
#
#
#


# Java
# Apple -> (compiler) apple.class -> (interpreter) (byte code)


# class Man:
#     name: str
#     surname: str
#
#     def __init__(self, person_name, person_surname):
#         self.name = person_name
#         self.surname = person_surname
#
#     def display(self):
#         print("Hello", self.name, self.surname)
#
#
# abc = Man("Ram", "Sharma")
# abc.display()


# class Person:
#
#     def __init__(self, person_name):
#         self.name = person_name
#
#
#     def display(self):
#         print(self.name)
#
#
# obj = Person("Ram")
# obj.display()


