def Cheer(x):
    print("How do you spell winner ?")
    print("I know! I know!")
    for i in x:
        print(i.capitalize(),end=(" "))
    print("! ")
    print("And that's how you spell winner!")
    print("Go", x.title(),"!")
Cheer('usman')