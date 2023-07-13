class Person:
    age = 25

    @classmethod
    def print_age(cls):
        print(cls.age)


# Person.print_age = classmethod(Person.print_age)
Person.print_age()
