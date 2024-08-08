
# Abstraction and Encapsulation (Trừu tượng và Đóng gói)
# 1. Abstraction (Trừu tượng):
# Tính trừu tượng là che giấu thông tin không cần thiết và chỉ hiển thị thông tin cần thiết cho người dùng.
# Có nghĩa là phải thiết kế module rõ ràng, dễ hiểu và dễ sử dụng.
# 2. Encapsulation (Đóng gói):
# Encapsulation là quá trình che giấu thông tin, bảo vệ dữ liệu của một đối tượng khỏi sự thay đổi từ bên ngoài.
# Kiểm soát quyền truy cập qua các mức độ truy cập (public, protected, private). Có thể truy cập thông qua các phương thức getter và setter.
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price, 0)
        
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
        
phone1 = Phone('Nokia', '1100', 5000)