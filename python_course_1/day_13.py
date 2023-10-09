# def upper_text(abc):
#     def wrapper():
#         return abc().upper()
#     return wrapper
#
#
# @upper_text
# def say_hello():
#     return "Hello world"
#
#
# print(say_hello())


# class Person:
#
#     def __init__(self, name):
#         self.first_name = name
#         print("Hello world", self.first_name)
#
#     def display(self):
#         print(self.first_name)
#
#
# obj = Person("Ram")
# obj.display()


# class Employee:
#
#     def __init__(self):
#         print("Hello world")
#
#     def __str__(self):
#         return "This is an employee class object"
#
#     def call(self):
#         print("this is call function")
#
# obj = Employee()
# print(obj)
# obj.call()


# class Men:
#     gender = "male"
#
#     # def __str__(self) -> str:
#     #     return "Hello"
#
#     # def display(self) -> str:
#     #     return "Hello"
#     #
#     # def call(self, name: int):
#     #     print(type(name))
#
#
# obj = Men()
# obj.call("a")
# print(obj)
# print(type(obj.display()))
# print(obj.gender)


class Men:

    gender = "male"


obj = Men()
obj.gender = "Female"
# del obj
print(obj.gender)


# del obj.gender
#
# print(obj.gender)

# print(obj.gender)
#
# obj.gender = "female"
# print(obj.gender)


# class Parent:
#
#     def display(self):
#         print("Parent class method")
#
#
# class Child(Parent):
#     pass
#
#
# obj = Child()
# obj.display()


# class A:
#     def method_a(self):
#         print("class a method")
#
#
# class B(A):
#     def method_b(self):
#         print("class b method")
#
#
# class C(B):
#     def method_c(self):
#         print("class c method")
#
#
# obj = C()
# obj.method_a()


# class A:
#     def method_a(self):
#         print("class a method")
#
#
# class B:
#     def method_b(self):
#         print("class b method")
#
#
# class C(A, B):
#     def method_c(self):
#         print("class c method")


# obj = C()
# obj.method_a()
# obj.method_b()


# class A:
#     def method_a(self):
#         print("class a method")
#
#
# class B(A):
#     def method_b(self):
#         print("class b method")
#
#
# class C(A):
#     def method_c(self):
#         print("class c method")
#
# obj_b = B()
# obj_b.method_a()
#
# obj_c = C()
# obj_c.method_a()



# class A:
#     def method_a(self):
#         print("class a method")
#
#
# class B(A):
#     def method_b(self):
#         print("class b method")
#
#
# class C(A):
#     def method_c(self):
#         print("class c method")
#
#
# class D(B):
#     def method_d(self):
#         print("class d method")



class A:

    def display(self):
        print("class a method")


class B(A):
    pass


obj = B()
obj.display()

