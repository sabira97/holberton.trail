class Sport:
    def __init__(self, name):
        self.name = name
    def play(self):
        return f"{self.name} oynanır"
class Football(Sport):
    def play(self):
        return f"{self.name}: Topla oynanır"
class Basketball(Sport):
    def play(self):
        return f"{self.name}: Topu səbətə atmaq"
class Chess(Sport):
    def play(self):
        return f"{self.name}: Zəka oyunu"
# İstifadə
f = Football("Futbol")
b = Basketball("Basketbol")
c = Chess("Şahmat")
print(f.play())
print(b.play())
print(c.play())