class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bloom(self):
        print(f"{self.name} gulu {self.color} rengde açir.")
class Rose(Flower):
    def bloom(self):
        print(f"Qirmizi {self.name} çox gözel açir!")
class Tulip(Flower):
    def bloom(self):
        print(f"{self.color} rengli {self.name} bahari xəbər verir.")
# İstifadə nümunəsi
flowers = [Rose("Gul", "qirmizi"), Tulip("Lale", "sari")]
for flower in flowers:
    flower.bloom()