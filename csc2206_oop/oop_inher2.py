class Animal(object):
    def __init__(self, name, color, specie):
        self.name = name
        self.color = color
        self.specie = specie
    
    def sound(self):
        return f"{self.name} is making a sound"
    
class Human(Animal):
    def __init__(self, name, color, specie, age):
        super().__init__(name, color, specie)
        self.specie = age

    def p_sound(self):
        return f"My name is {self.name} and I am talking"
    

abi = Human("Paul", "Dark", "Mammals", 24)

print(abi.color)
print(abi.sound())                                                              
print(abi.p_sound())