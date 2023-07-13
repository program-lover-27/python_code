def my_decorator(func):
    def wrapper():
        return func().upper()

    return wrapper


@my_decorator
def say_hello():
    return "Hello World"


print(say_hello())
