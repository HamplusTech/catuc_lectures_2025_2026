class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return "This animal is eating."

class Dog(Animal):
    def sound(self):
        return f"This is a {self.name} and the sound is Barks"
    
class Cat(Animal):
    def sound (self):
        return f"This is a {self.name} and the sound is Meow"
    

animal1 = Dog("Dog")
animal2 = Cat("Cat")

print(animal1.sound(),"\n", animal2.sound())