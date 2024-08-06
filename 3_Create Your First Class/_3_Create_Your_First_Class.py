
class Student:
    # Hàm khởi tạo (constructor) được gọi khi tạo một đối tượng mới từ class)
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

# Tạo một đối tượng từ class Student (Object)
student1 = Student('Lam Nghia', 1, 500)
print(student1.name)