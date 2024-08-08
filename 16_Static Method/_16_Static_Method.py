class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    # Static method (phương thức tĩnh) trong Python là một phương thức thuộc về lớp (class) 
    # Nhưng không truy cập hoặc sửa đổi trạng thái của lớp đó
    # Static method không có tham số self hay cls. Không thể truy cập hoặc thay đổi trạng thái của lớp hoặc instance
    # Dùng Static method khi có một hàm mà logic của nó liên quan đến lớp, nhưng không cần truy cập hoặc thay đổi trạng thái của lớp hoặc instance.
    @staticmethod
    def printStatement():
        print('This is a static method')
        
s1 = Student('Alex', 20)
s1.printStatement()
# Static method có thể được gọi trên lớp mà không cần tạo instance của lớp đó
Student.printStatement()

# Lưu ý: Có thể hiểu đơn giản object = instance
