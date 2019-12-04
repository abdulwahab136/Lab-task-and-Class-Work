def numbers(x,y):
    print("decimal    binary    octal   Hexadecimal")

    for i in range(x,y+1):
        binary = bin(i)
        octal = oct(i)
        Hex = hex(i)
        print("d:{:5d}   b:{:5b}   o:{:5o}   H:{:5X}".format(i,i,i,i))
numbers(1,10)
