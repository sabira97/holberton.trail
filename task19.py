class Animal:
    def speak(self):
        print("Animal sound")
class Cat(Animal):
    def speak(self):
        print("Meow :smiley_cat:")
class Dog(Animal):
    def speak(self):
        print("Woof :dog:")
Dog().speak()