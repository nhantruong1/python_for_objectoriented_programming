# MRO (Method Resolution Order)
# là một cơ chế trong Python để xác định thứ tự các lớp được tìm kiếm khi gọi một phương thức hoặc truy cập một thuộc tính

# Method Overriding
# là một cơ chế trong Python cho phép một lớp con ghi đè một phương thức của lớp cha.


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

    # Method Overriding
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"
        
class FlagShip(Smartphone):    # Derived Class / Child Class
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rare_camera) # Common Method
        self.front_camera = front_camera
        
phone1 = Phone('Nokia', '1100', 1000)
smartphone1 = Smartphone('OnePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
samsung = FlagShip('Samsung', 'Galaxy S10', 50000, '8 GB', '128 GB', '20 MP', '16 MP')
print(samsung.full_name())