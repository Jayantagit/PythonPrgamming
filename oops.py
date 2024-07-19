class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getMarks(self):
        return self.name,":",self.marks

    @staticmethod
    def getColledge():
        return "Jadavpur University"

    @classmethod
    def getGrade(cls):
        return "A"

stud1=Student("Jayanta",98)
print(stud1.getMarks())
print(Student.getColledge())
print(Student.getGrade())
print(stud1.getGrade())
