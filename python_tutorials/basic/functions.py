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
