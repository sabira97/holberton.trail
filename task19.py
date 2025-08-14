class Animal:
    def speak(self):
        print("Animal sound")
class Horse(Animal):
    def speak(self):
        print("Neigh :horse:")
class Elephant(Animal):
    def speak(self):
        print("Trumpet :elephant:")
    
Elephant().speak()