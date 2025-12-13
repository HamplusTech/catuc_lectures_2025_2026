from abc import ABC, abstractmethod

class Vehicle (ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."
    
class Plane(Vehicle):
    def move(self):
        return "The plane flies in the sky"
    
vehicles = [Car(), Plane()]
for v in vehicles:
    print(v.move())