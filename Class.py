#Class

class Student:
    def __init__(self, name, finished = False):
        self.name = name
        self.finished = finished




student = Student("John")
print(student.name)
print(student.finished)

# Ülesanne: klassi konstruktor

"""Constructor exercise."""

class Empty:
    """An empty class without constructor."""
    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
        pass

class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty = Empty()
""
    # 3 x person usage
    person_1 = Person()
    person_1.firstname = "John"
    person_1.lastname = "Wick"
    person_1.age = 12

    person_2 = Person()
    person_2.firstname = "Malle"
    person_2.lastname = "Nali"
    person_2.age = 36

    person_3 = Person()
    person_3.firstname = "Madis"
    person_3.lastname = "Damuni"
    person_3.age = 69
    # 3 x student usage
    student_1 = Student("Kaur", "Rusikas", 9)
    student_2 = Student("Mati", "Mustikas", 23)
    student_3 = Student("Anti", "Silm", 60)
    pass


