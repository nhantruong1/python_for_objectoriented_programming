class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= 500:
            return "Pass"
        else:
            return "Fail"
     
s1 = Student("Lam Nghia", 500)
s3 = Student("Hoai Thanh", 400)
s4 = Student("Lam Trach", 700)
s5 = Student("Thanh Thuy", 800)

student_objects = [s1, s3, s4, s5]
passStudents = []
failStudents = []
students_result = {}
for x in student_objects:
    if x.result() == "Pass":
        passStudents.append(x.name)
        students_result['Pass Students'] = passStudents
    else:
        failStudents.append(x.name)
        students_result['Fail Students'] = failStudents

print(students_result)