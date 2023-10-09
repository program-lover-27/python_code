# class A:
#     def function_a(self):
#         print("Function call from class A.")
#
#
# class B:
#
#     def function_a(self):
#         print("Function call from class B.")
#
#
# class C(B, A):
#     def function_c(self):
#         self.function_a()
#         # self.function_b()
#         # print("Function call from class C.")
#
#
# obj = C()
# obj.function_c()


# class A:
#
#     def __init__(self):
#         print("Non parameterize constructor")
#
#     def __init__(self, name):
#         print("Parameterize constructor")
#
# obj = A()

#
# class A:
#
#     def __init__(self, name):
#         print("Class A init function")
#
#     def display(self):
#         print("Class A display function")
#
# class B(A):
#
#     def __init__(self):
#         # super().__init__("Ram")
#         A.__init__(self, "Ram")
#         # super().display()
#         A.display(self)
#         # print("Class B init function")
#
#
# obj = B()
# obj.display()


# class A:
#
#     def __init__(self):
#         print("Class A init function")
#
#     def display(self):
#         print("class A display method")


# class B(A):
#
#     def __init__(self):
#         print("Class B init function")
#         self.display()
#         # A.display(self)
#         # super().display()
#
#     def display(self):
#         print("class B display method")
#
#
# obj = B()
# obj.display()


# def display(*args, **kwargs):
#     print("Display func 2")
#
# display()


# class A:
#     def display(self):
#         print("class A display")
#
# class B(A):
#
#     def __init__(self):
#         print("class B constructor")
#         super().display()
#
#     def display(self):
#         print("class B display")
#
# class C(B):
#     def __init__(self):
#         super().display()
#
#     def display(self):
#         print("class C display")
#
# obj = C()


# class A:
#     def add(self, *data):
#         sum = 0
#         for num in data:
#             sum = num + sum
#         return sum
#
#     # def add(self, number_1, number_2, number_3):
#     #     return number_1 + number_2 + number_3
#
# obj = A()
#
# print(obj.add(1, 2))
# print(obj.add(1, 2, 3))


# class Animal:
#
#     def sound(self):
#         print("No sound")
#
# class Dog(Animal):
#
#     def sound(self):
#         print("Woof, Woof")
#
# class Cat(Animal):
#
#     def sound(self):
#         print("Meauoo, Meauoo")
#
#
# class Man(Animal):
#     pass

class A:
    __name = "Ram"
    _surname = "Sharma"
    fullname = "Ram Sharma"

class B(A):

    def __init__(self):
        print(self._surname)


# obj = A()
obj = B()
# print(obj.__name)
print(obj._surname)
# print(obj._surname)
# print(obj.fullname)



