#Task 3
class house:
    def __init__(self,room,rent,parking,location):

        self.room = room
        self.parking = parking
        self.location=location
        self.rent = rent
    def location(self,location):
        self.location = location


class Banglow(house):
    def details(self,area):
        print("Number of Rooms : ",self.room)
        print("Rent Cost : ",self.rent,"$")
        print("Parking Available or Not : ",self.parking)
        print("Area of Banglow : ",area ,"square yards")

class Flats(house):
    def details(self,area):
        print("Number of Rooms : ",self.room)
        print("Rent Cost : ",self.rent,"$")
        print("Parking Available or Not : ",self.parking)
        print("Area of Banglow : ",area ,"square yards")

flat1 = Flats("5",500,"yes","Tariq Road")
Banglow1 = Banglow(12,10000,'yes','Bahadurabad')

print(flat1.details("300"))
print(Banglow1.details(800))
