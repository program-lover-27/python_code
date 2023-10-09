# try:
#
#     # value = 10 / 0
#     value = int("a")
#     print(value)
#
# except ZeroDivisionError as e:
#     print("Exception 1", e)
# except Exception as e:
#     print("Exception", e)
#
# print("Division completed")


# try:
#     value = int(input("Enter positive number "))
#     print(value)
# except Exception as e:
#     print("Exception:", e)
# else:
#     print("Exception not occur")
# finally:
#     print("Finally always be executed")
#
#
# print("Division completed")


# file = None
# try:
#
#     file = open("exam.txt", "r")
#
# except FileExistsError as e:
#     print("Exception 1", e)
#
# except FileNotFoundError as e2:
#     print(e2)
#
# except Exception as e1:
#     print("Exception", e1)
#
#
# finally:
#     if file:
#         file.close()
#     print("Finally block")


# class Exception:
#     def __init__(self):
#         pass
#
# class FileNotFoundError(Exception):
#     def __init__(self):
#         pass


class CustomError(Exception):

    def __init__(self, message):
        super().__init__(message)


try:
    age = 20
    if age < 18:
        raise CustomError("You are not eligible for vote")
except CustomError as e:
    print("Exception:", e)

print("Hello world")

# age = 15
# if age < 18:
#     raise CustomError("You are not eligible for vote")
#
# print("Hello world")

#
# try:
#     file = open("example.txt", "r")
#     print(type(file))
#     file.close()
#     file.read()
#
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)


# try:
#     value = 0
#     if value == 0:
#         raise Exception("Value is less than zero")
# except Exception as e:
#     print(e)

# try:
#     value = int(input("Enter a positive number "))
#     try:
#         new_value = value / 0
#     except ZeroDivisionError as e1:
#         print("Exception 0:", e1)
# except Exception as e:
#     print("Exception 1:", e)
