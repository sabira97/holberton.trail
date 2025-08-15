class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed increased to {self.speed} km/h")
    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Speed decreased to {self.speed} km/h")
car = Car("Range Rover")
car.accelerate(30)
car.brake(10)