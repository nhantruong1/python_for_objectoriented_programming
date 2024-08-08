
# Inheritance (Tính kế thừa) trong Python
# Inheritance cho phép một lớp (class) mới được tạo ra (con) bằng cách sử dụng thông tin đã được xác định trong lớp khác (cha).
# Lớp con kế thừa tất cả các phương thức và thuộc tính từ lớp cha.
# Lớp con có thể thay đổi hoặc mở rộng chúng.
# Lớp cha còn được gọi là lớp cơ sở hoặc lớp cha.
# Lớp con còn được gọi là lớp dẫn xuất hoặc lớp con.
# Lớp con có thể thừa hưởng từ nhiều lớp cha.



class Phone:    # Base Class / Parent Class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price, 0)
        
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
class Smartphone(Phone):    # Derived Class / Child Class
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera):
        super().__init__(brand, model_name, price) # Common Method
        # Phone.__init__(self, brand, model_name, price)    # Uncommon Method
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera
        
phone1 = Phone('Nokia', '1100', 5000)
smartphone1 = Smartphone('OnePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
print(smartphone1.full_name())