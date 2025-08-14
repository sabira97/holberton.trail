from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} AZN with card :credit_card:")
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} AZN in cash :dollar:")
CardPayment().pay(200)
CashPayment().pay(50)