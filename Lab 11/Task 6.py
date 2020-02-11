class teacher:
    def __init__(self,name,department,exp):
        self.name = name
        self.department = department
        self.exp = exp

    def description(self):
        print("Name of Teacher : ",self.name)
        print("Department of Teacher : ",self.department)
        print("Experience of Teacher : ",self.exp , "Years")

Iqbal = teacher("Iqbal",'SE',23)
print(Iqbal.description())

class students:
    def __init__(self,name , department,semester):
        self.name = name
        self.department = department
        self.semester = semester
    def description(self):
        print("Name of Student  : ",self.name)
        print("Department of Student : ",self.department)
        print("Semester of Student  : ",self.semester )

samad = students("Abdul Samad","CS",'V')
print(samad.description())