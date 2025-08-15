from abc import ABC, abstractmethod
# 4. Abstraction
class Employee(ABC):
    def __init__(self, name, salary):
        # 1. Encapsulation
        self.name = name
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
class Manager(Employee):
    def work(self):
        return f"{self.name} komandaya rəhbərlik edir :clipboard:"
# Şirkət sinfi (Encapsulation + obyekt idarəsi)
class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []  # private list
    def add_employee(self, employee):
        self.__employees.append(employee)
    def show_all_employees(self):
        for emp in self.__employees:
            print(emp.work(), "| Maaş:", emp.get_salary())
# İstifadə
company = Company("Holberton Tech")
company.add_employee(Developer("Səbirə", 3000))
company.add_employee(Designer("Aynur", 2500))
company.add_employee(Manager("Sehane", 4000))
company.show_all_employees()