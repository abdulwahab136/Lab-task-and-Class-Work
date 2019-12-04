def comparing():
    PSOP , PSOHSD , PSOLSD , PSOKO = 114.24,127.41,85.33,97.18
    SAP , SAD , SLDO , SSKO = 114.24,127.41,85.33,97.18
    petrol = eval(input("Ammount Of Petrol :"))
    HDiesel = eval(input("Ammount of High Speed Diesel :"))
    LDiesel = eval(input("Ammount of Low Speed Diesel :"))
    Kerosine = eval(input("Ammount of Kerosine Oil :"))
    print("\t\tPSO\t\t\t\t\t\t\t\t\tShell\t\t\t\tAmmount in Litres\t\t\tPSO Cost\t\tShell Cost\t\tPrice Difference ")
    print("Premium Super     : {0}\t\t\tAltron Premium: {1}\t\t\t\t{2}\t\t\t\t\t{3}\t\t\t{4}\t\t\t\t{5}".format(PSOP,SAP,petrol,PSOP*petrol,SAP*petrol,(PSOP-SAP)*petrol))
    print("HighSpeed Diesel  : {0}\t\t\tAction+Diesel : {1}\t\t\t\t{2}\t\t\t\t\t{3}\t\t\t{4}\t\t\t\t{5}".format(PSOHSD, SAD,HDiesel, PSOHSD*HDiesel,SAD*HDiesel,(PSOHSD-SAD)*HDiesel))
    print("LightSpeed Diesel : {0}\t\t\tLDO           : {1}\t\t\t\t{2}\t\t\t\t\t{3}\t\t\t{4}\t\t\t\t{5}".format(PSOLSD, SLDO,LDiesel, PSOLSD*LDiesel,SLDO*LDiesel,(PSOLSD-SLDO)*LDiesel ))
    print("LightSpeed Diesel : {0}\t\t\tLDO           : {1}\t\t\t\t{2}\t\t\t\t\t{3}\t\t\t{4}\t\t\t\t{5}".format(PSOKO,SSKO,Kerosine,PSOKO*Kerosine,SSKO*Kerosine,(PSOKO-SSKO)*Kerosine))

comparing()