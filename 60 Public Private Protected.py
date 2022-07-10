# Public Access Modifier:

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Protected Access Modifier:

class Student:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age  # protected attribute

# Private Access Modifier:

class Teacher:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age  # private attribute

har = Teacher("Harshit",21)
print(har._Teacher__name)