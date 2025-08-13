class CreditCard:
    def __init__(self, Aynur, pin):
        self.Aynur = Aynur
        self.__pin = pin
    def check_pin(self, pin):
        return pin == self.__pin
card = CreditCard("Səbirə", "5678")
print(card.check_pin("5678"))  