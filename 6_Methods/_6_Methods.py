
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def result(self):
        if self.marks > 500:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Lam Nghia", 21, 500)
print(s1.result())
