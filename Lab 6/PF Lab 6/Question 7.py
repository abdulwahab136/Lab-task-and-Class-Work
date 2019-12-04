import time
def POS():
    User = input("Enter User Name :")
    x = input("Enter the type of Burger : ")
    y = eval(input("Enter the Quantity of Burger : "))
    z = eval(input("Enter the rate of Burger : "))
    total = y * z
    gst = (total/100)*17
    time1= time.strftime('%b %d %Y', time.localtime())
    print(time1)
    print("User Name :          ",User)
    print("Type of Burger:      ",x)
    print("Quantity of Burger:  " ,y)
    print("Cost :               ",total)
    print("GST 13% :            ",gst)
    print("Total :            Rs",total+gst)
POS()