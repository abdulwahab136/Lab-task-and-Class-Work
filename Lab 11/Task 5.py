class plant:
    def __init__(self,name,area,size,smell):
        self.name = name
        self.area = area
        self.size = size
        self.smell = smell
    def description(self):
        print("Name of Plant : ",self.name)
        print("Area of Plant : ",self.area)
        print("Size of plant : ",self.size)
        print("Smell of Plant : ",self.smell)

class Fruit(plant):
    def details(self,Fruit,taste):
        print(plant.description(self))
        print("Fruit Name : ",Fruit)
        print("Taste of Fruit : ",taste)

class nonfruit(plant):
    def details(self,wood):
        print(plant.description(self))
        print("Wood Type : ",wood)

mapple = nonfruit('mapple','Northern Area','50','pungent')

mapple.details("Sturdy")