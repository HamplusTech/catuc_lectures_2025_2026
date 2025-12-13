class Car:
    def __init__(this, brand, name):
        this.brand = brand
        this.name = name

    def move(self):
        return f"Driving"

class Ship:
    def __init__(this, brand, name):
        this.brand = brand
        this.name = name

    def move(self):
        return f"Sailing"

class Plane:
    def __init__(this, brand, name):
        this.brand = brand
        this.name = name

    def move(self):
        return f"Flying"
    

mob1 = Car("Sienna", "Toyota")
mob2 = Ship("Bismarck", "Cargo")
mob3 = Plane("Boeing 737", "Boeing")

# mobilities = [mob1.brand, mob2.brand, mob3.brand] 
# mobilities = [mob1.move(), mob2.move(), mob3.move()] 
mobilities = [mob1, mob2, mob3] 

# mobilities = [Car("Sienna", "Toyota"), Ship("Bismarck", "Cargo"), Plane("Boeing 737", "Boeing")]

# print("There are three different behaviours of the object. These are behaviour:")
# for mobility in mobilities:
#     print(f"{mobility}")

# print("There are three different behaviours of the object. These are behaviour:")
# for mobility in mobilities:
#     print(f"{mobility.move()}")

print("There are three different behaviours of the object. These are behaviour:")
for x in range(len(mobilities)):
    print(f"Behaviour {x + 1} - {mobilities[x]}")