def printv(x):
    fees = {'Name': '', 'RollNo': '434', 'Semester': '6',
            'SemesterFee': '12000', 'SportsFee': '2500', 'MiscFee': '0'}
    fees['Name'] = x
    Sum = int(fees.get('SemesterFee')) + int(fees.get('SportsFee')) + int(fees.get('MiscFee'))
    print(" \t\tBank Copy\t\t\t\t\t School Copy\t\t\t\t\t\tStudent Copy")
    print("Student Name : {0}\t\tStudent Name : {0}\t\tStudent Name : {0}".format(fees.get('Name')))
    print("Roll Number  : {0}\t\t\t\tRoll Number  : {0}\t\t\t\tRoll Number  : {0}".format(fees.get('RollNo')))
    print("Semester     : {0}\t\t\t\tSemester     : {0}\t\t\t\tSemester     : {0}".format(fees.get('Semester')))
    print("Semester Fee : {0}\t\t\tSemester Fee : {0}\t\t\tSemester Fee : {0}".format(fees.get('SemesterFee')))
    print("Sports Fee   : {0}\t\t\t\tSports Fee   : {0}\t\t\t\tSports Fee   : {0}".format(fees['SportsFee']))
    print("Misc Fee     : {0}\t\t\t\tMisc Fee     : {0}\t\t\t\tMisc Fee     : {0}".format(fees.get('MiscFee')))
    print("--------------- \t\t\t    ------------------- \t\t\t---------------------")
    print("Total Fee     : {0}\t\t\tTotal Fee     : {0}\t\t\tTotal Fee    : {0}".format(Sum))
    print("Due Date     : 12-12-19\t\t\tDue Date     : 12-12-19\t\t\tDue Date     : 12-12-19")
    print("Teller Stamp : ____________\t\tTeller Stamp : ____________\t\tTeller Stamp : ____________")
    print('\n')
printv('Abdul Wahab')
printv('Adnan Samad')
printv('Omer Siddqui')