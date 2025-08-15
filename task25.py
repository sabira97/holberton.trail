from abc import ABC, abstractmethod
# 4. Abstraction - Ümumi işçi sinfi
class Worker(ABC):
    def __init__(self, name, daily_rate):
        # 1. Encapsulation
        self.name = name
        self.__daily_rate = daily_rate
    def get_daily_rate(self):
        return self.__daily_rate
    @abstractmethod
    def work(self):
        pass
# 2. Inheritance + 3. Polymorphism
class Engineer(Worker):
    def work(self):
        return f"{self.name} tikinti planı hazırlayır :triangular_ruler:"
class Builder(Worker):
    def work(self):
        return f"{self.name} divar tikir :bricks:"
class Electrician(Worker):
    def work(self):
        return f"{self.name} elektrik sistemi quraşdırır :zap:"
# Tikinti şirkəti
class ConstructionCompany:
    def __init__(self, name):
        self.name = name
        self.__workers = []  # private list
    def add_worker(self, worker):
        self.__workers.append(worker)
    def show_workers(self):
        for w in self.__workers:
            print(w.work(), "| Günlük maaş:", w.get_daily_rate())
# İstifadə
company = ConstructionCompany("Gence İnşaat MMC")
company.add_worker(Engineer("Səbirə", 220))
company.add_worker(Builder("Aynur", 90))
company.add_worker(Electrician("Sabina", 110))
company.show_workers()