
class Student:
    totalMarks = 1000
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.totalMarks = Student.totalMarks
        
s1 = Student("Lam Nghia", 21, 500)
s2 = Student("Hoai Thanh", 22, 400)
s3 = Student("Lam Trach", 23, 700)
s4 = Student("Thanh Thuy", 24, 800)

print(s1.totalMarks)