# class Math:
#     def add(slef, numb_1, numb_2):
#         return numb_1 + numb_2
#
#     def add(slef, numb_1, numb_2, numb_3):
#         return numb_1 + numb_2 + numb_3
#
#
#     def python_function(*args):
#         for i in range(len(args)):
#             print("The company name is", args[i])
#
#
#     python_function("Google", "Microsoft", "Amazon", "ajnsjkdnsdk")


# class A:
#     def display(self):
#         pass
#
#
# class B(A):
#     def display(self):
#         pass


# class A:
#     name: str
#     _name: str
#     __name: str
#
#     def display(self):
#         pass
#
#     def _display(self):
#         pass
#
#     def __display(self):
#         pass
#
# class B(A):
#     pass

# class Employee:
#     __name: str
#
#     def set_name(self, name):
#         self.__name = "Mr." + name
#
#     def get_name(self):
#         return self.__name


# file = open("/Users/teslaindtechnology/Desktop/example_1.txt", "r")
# print(file.read())
# print(file.readlines())
# print(file.readline())


# file = open("/Users/teslaindtechnology/Desktop/example_1.txt", "w")

# file = open("/Users/teslaindtechnology/Desktop/example_1.txt", "a")
#
# file.write("\nHello Shyam")
# print(file.read())


# file = open("/Users/teslaindtechnology/Desktop/example_1.txt", "w+")
# file.write("Hello Shyam\n")
# print(file.read())
#
# file.close()


# file = open("Users/teslaindtechnology/Desktop/example.txt", "w+")

# with open("/Users/teslaindtechnology/Desktop/example_1.txt", "r") as file:
#     file.write("Hello world")


# import hello
# from temp import hello
# from temp.hello import say_hello, welcome, welcome_1
# from temp.hello import *

# from temp import hello, welcome


# def say_hello():
#     print("Say hello function")
#
# def welcome():
#     print("Welcome")
#
#
# def welcome_1():
#     print("Welcome")
#
# # from temp.hello import *
# # from temp.welcome import *
#
# if __name__ == "__main__":
#     # hello.say_hello()
#     say_hello()
#     welcome()
#     welcome_1()
