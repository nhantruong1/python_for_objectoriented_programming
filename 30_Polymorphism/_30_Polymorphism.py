# Polymorphism (Tính đa hình)
# Polymorphism là một khái niệm trong lập trình hướng đối tượng, 
# Nó cho phép chúng ta gọi cùng một phương thức trên các object khác nhau mà không cần quan tâm đến loại object đó.
# Polymorphism giúp chúng ta viết code linh hoạt hơn, dễ dàng mở rộng và bảo trì.

# Ví dụ:
# 2 + 3 = 5
# '2' + '3' = '23'

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
    
    def __add__(self, other):
        return "In Phone: " + str(self.price + other.price)
    
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
    
    def __add__(self, other):
        return "In SmartPhone: " + str(self.price + other.price)
        
class FlagShip(Smartphone):    # Derived Class / Child Class
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rare_camera) # Common Method
        self.front_camera = front_camera
    
    def __add__(self, other):
        return "In FlagShip: " + str(self.price + other.price)
        
phone1 = Phone('Nokia', '1100', 1000)
phone2 = Phone('Nokia', '1600', 2000)
smartphone1 = Smartphone('OnePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
smartphone2 = Smartphone('OnePlus', '6', 40000, '8 GB', '128 GB', '20 MP')
flagship1 = FlagShip('Samsung', 'Galaxy S10', 50000, '8 GB', '128 GB', '20 MP', '16 MP')
flagship2 = FlagShip('Samsung', 'Galaxy S20', 60000, '12 GB', '256 GB', '20 MP', '16 MP')

print(phone1 + phone2)
print(smartphone1 + smartphone2)
print(flagship1 + flagship2)

