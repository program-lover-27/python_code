# __name__ = "main"
# print(__name__)
#


# __init__ = "init call"
# print(__init__)

# class = "class var" # Not allowed


# class A:
#     def __init__(self):
#         print("class A init constructor")
#
#
# class B(A):
#     def __init__(self):
#         print("class B init constructor")
#
#
# class C(B):
#     def __init__(self):
#         super(B, self).__init__()
#         # A.__init__(self)
#         # super().__init__()
#         print("class C init constructor")
#
#
# if __name__ == "__main__":
#     obj = C()


# class A:
#     def __init__(self):
#         print("A")
#
#     def display(self):
#         print("class A Display")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#     def display(self):
#         print("class B Display")
#
#
# class C(A):
#     def __init__(self):
#         print("C")
#
#     def display(self):
#         print("class C Display")
#
#
# class D(C, B):
#     def __init__(self):
#         print("D")
#         self.display()
#
#
# obj = D()


# class A:
#
#     # def add(self, num_1, num_2):
#     #     return num_1 + num_2
#     #
#     # def add(self, num_1, num_2, num_3):
#     #     return num_1 + num_2 + num_3
#
#     def add(self, *data):
#         return sum(data)
#
#
# obj = A()
# print(obj.add(1, 2, 3, 4, 5))


# class A:
#     def display(self):
#         print("class A")
#
#
# class B(A):
#     def display(self):
#         print("class B")
#
#
# obj = B()
# obj.display()


# class Animal:
#     def sound(self):
#         print("No sound")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("Meauooo")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("Bhooooo")
#
#
# class Man(Animal):
#     pass
#
#
# Cat().sound()
# Dog().sound()
# Man().sound()


# class Bank:
#     def get_interest_rate(self):
#         return 0
#
#
# class Axis(Bank):
#     def get_interest_rate(self):
#         return 5.5
#
#
# class SBI(Bank):
#     def get_interest_rate(self):
#         return 6.0
#
# print(Axis().get_interest_rate())
# print(SBI().get_interest_rate())


# class Demo:
#     name = "Apple" # public
#     _name = "Peru" # protected
#     __name = "Chiku" # private
#
# class Demo1(Demo):
#     def __init__(self):
#         print(self._name)
#     pass
#
# # print(Demo().name)
# # print(Demo1()._name)
#
# print(Demo().__name)


# class Person:
#     __age: int
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__age
#
#
# obj = Person()
# obj.set_age(10)
# print(obj.get_name())


# class Circle:
#     __radius = 0
#
#     def set_radius(self, radius):
#         self.__radius = radius
#
#     def get_area(self):
#         pi = 3.14
#         return self.__radius * self.__radius * pi
#
#
# obj = Circle()
# obj.set_radius(5)
# print(obj.get_area())


# class Man:
#     __name = ""
#     __age = 0
#     __div = ""
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_div(self, div):
#         self.__div = div
#
#     def get_div(self):
#         return self.__div
#
#
# class Person:
#     # def __init__(self, abc: Man):
#     #     print(abc.get_name())
#     #     print(abc.get_age())
#
#     def __init__(self, name, age, div):
#         print(name, age)
#         print(div)
#
#
# class Gender:
#     def __init__(self, name, age, div):
#         print(name, age)
#         print(div)
#
#
# obj = Man()
# obj.set_name("Ram")
# obj.set_age(20)
# obj.set_age("10th")
#
# # Person(obj)
#
# Person("Ram", 20, "10th")


# class Person:
#     __name = ""
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return "Mr. " + self.__name
#

#
# obj = Person()
# obj.set_name("Ram")
# # print("Mr. " + obj.name)
# print(obj.get_name())
#
# obj_1 = Person()
# obj_1.set_name("Shyam")
# # print("Mr. " + obj_1.name)
# print(obj_1.get_name())


# class Person:
#     name = ""
#     _name = ""
#     __name = ""
#
#     def get_name(self):
#         print("public function")
#
#     def _get_name(self):
#         print("protected function")
#
#     def __get_name(self):
#         print("private function")
#
#
# obj = Person()
# obj.get_name()


# obj._get_name()
# obj.__get_name()


# class Person:
#     _name = ""
#
#     def set_name(self, name):
#         self._name = "Mr. " + name
#
#     def get_name(self):
#         return self._name


# obj = Person()
# obj.set_name("Ram")
# print(obj.get_name())

# class Man(Person):
#     def __init__(self):
#         self.set_name("Ram")
#         print(self.get_name())
#
# obj = Man()
