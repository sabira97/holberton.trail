class Person:
    def __init__(self, age=0):
        self._age = age #protected atribut

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person()
p.set_age(27)
print(p.get_age())  # 27