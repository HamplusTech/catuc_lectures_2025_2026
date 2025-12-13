class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    

class Car:
    def __init__(self, name, model, color, year, type):
        self.name = name
        self.model = model 
        self.color = color
        self.year = year 
        self.type = type
        print (f"Creating a Car object with the name {self.name}")

    def __str__(self):
        return "Name = %s, Model = %s, Colour = %d" %(self.name,self.model, self.color)
    
    def accelerate(self, speed):
        return f"The car's speed has increase by {speed}"

    def driver (self, nameDriver):
        return f"This car with the model as {self.model} is driven by {nameDriver}"

# tanya = Person("Tanya",45)
# precious = Person("Precious", 54)
# nelson = Person ("Nelson Bruce", 99)

# # print(tanya.age)
# print(tanya.greet())
# print(precious.greet())
# print(nelson.greet())

car1 = Car("Toyota", "Siena", "black", 2023, "mini van")
# car2 = Car("Toyota", "Venza", "green", 2025, "suv")

# print(car1.type)
# print(type(car1))

# print(car1.accelerate(50))
print(car1.driver("Paul"))
# print(car2.driver("Douglas"))