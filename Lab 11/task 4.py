class toyota:
    def __init__(self,model,make,color,price,type):
        self.model = model
        self.make = make
        self.color = color
        self.price = price
        self.type = type

    def description(self):
        print("Model of Car : ",self.model)
        print("Make of Car : ",self.make)
        print("Color of Car : ",self.color)
        print("Price of Car : ",self.price)
        print("type of Car : ",self.type)

class sedan(toyota):
    def details(self,seating):
        print("Seating Capacity : ",seating)

class SUV(toyota):
    def details(self,suspensions):
        print("suspensions dimensions : ",suspensions)

class Hatchback(toyota):
    def details(self,trunk):
        print("Trunk Dimensions",trunk)

class Truck(toyota):
    def details(self,load):
        print("load capacity : ",load , "KGs")

Civic = sedan(2018,2017,'red',50000,'sports')

print(Civic.description())
print(Civic.details(5))