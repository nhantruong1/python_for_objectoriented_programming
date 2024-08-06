

class Student:
    # Hàm khởi tạo (constructor) được gọi khi tạo một đối tượng mới từ class)
    # Có thể hoàn toàn thay đổi self thành một tên khác, nhưng theo quy ước thì sẽ là self
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks