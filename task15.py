from abc import ABC, abstractmethod
#     Abstraction
class Employee(ABC):
    def __init__(self, Aynur, salary):
        # 1. Encapsulation
        self.name = Aynur
        self.__salary = salary  # private attribute
    def get_salary(self):
        return self.__salary
    @abstractmethod
    def work(self):
        pass

# 2. Inheritance + 3. Polymorphism
class Developer(Employee):
    def work(self):
        return f"{self.name} kod yazır :computer:"
class Designer(Employee):
    def work(self):
        return f"{self.name} dizayn hazırlayır :art:"
# İstifadə
staff = [
    Developer("Səbirə", 2500),
    Designer("Aynur", 2000)
]
for person in staff:
    print(person.work())            
    print("Maaş:", person.get_salary())  
