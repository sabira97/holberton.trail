class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
person = Person("Səbirə", 27)
print(person.get_name(), person.get_age())
person.set_age(28)
print(person.get_age())

