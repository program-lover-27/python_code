# Python Function Multiple Arguments
def python_function(name, country):
    print("Hello world")
    print(name)
    print(country)


python_function("John", "USA")


# Python Function Parameter With Default Value
def python_function(name, country="USA"):
    print("Hello world")
    print(name)
    print(country)


python_function("John")


# Python Function Keyword Arguments
def python_function(name, country):
    print(name)
    print(country)


python_function(country="USA", name="John")


# Pass List As an Argument To The Function
def python_function(input_list):
    for name in input_list:
        print(name)


name_list = ["John", "Smith"]

python_function(name_list)


# Python Arbitrary Arguments, *args
def python_function(*args):
    for name in args:
        print(name)


python_function("John", "Smith")


# Python Arbitrary Keyword Arguments, **kwargs
def python_function(**name):
    print(name)
    print(name["name"])
    print(name["country"])


python_function(name="John", country="USA")
