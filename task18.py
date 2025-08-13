class Vehicle:
    def move(self):
        print("Moving...")
class Car(Vehicle):
    def move(self):
        print("Car driving :car:")
class Plane(Vehicle):
    def move(self):
        print("Plane flying :airplane:")
Car().move()
Plane().move()