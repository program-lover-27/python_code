# Python treats everything as an object
def welcome(name):
    print(name)


welcome("John")

hello = welcome
hello("Smith")

hey = welcome
hey("Jacob")


# ------------------------
class Welcome:
    def __init__(self, name):
        print(name)


Welcome("John")

hello = Welcome
hello("John")


# ---------------------------------------------
# Pass Function As an Argument

def double(number):
    return number * number


def get_number(function, number):
    result = function(number)
    return result


print(get_number(double, 2))


# ---------------------------------------------
# Return a Function
def welcome():
    def greet():
        print("Welcome.")

    return greet


text = welcome()
text()


# ---------------------------------------------
# Decorator a Function
def my_decorator(func):
    def wrapper():
        return func().upper()

    return wrapper


@my_decorator
def say_hello():
    return "Hello World"


print(say_hello())


# ---------------------------------------------
# Python Decorator Function With Arguments
def text_decorator(function):
    def wrapper(arg1):
        return function(arg1.upper())

    return wrapper


def welcome_decorator(function):
    def greet(arg1):
        print("Welcome")
        return function(arg1)

    return greet


# Python Function With Multiple Decorators
@welcome_decorator
@text_decorator
def say_hello(name):
    return "Hello " + name


print(say_hello("John"))

