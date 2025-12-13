class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
class Cow:
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())