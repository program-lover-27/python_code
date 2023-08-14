def my_generator():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3


obj = my_generator()
try:
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
except StopIteration:
    print("StopIteration called successfully")


# -----
def my_generator():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3


obj = my_generator()

for number in obj:
    print(number)


# -----
def my_generator():
    print("first")
    yield 1
    print("second")
    yield 2
    return
    print("third")
    yield 3


obj = my_generator()

for number in obj:
    print(number)
