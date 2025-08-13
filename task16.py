class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
    def get_age(self):
        return self.__age
p = Person("Səbirə", 27)
print(p.get_age())  
p.set_age(28)
print(p.get_age())  