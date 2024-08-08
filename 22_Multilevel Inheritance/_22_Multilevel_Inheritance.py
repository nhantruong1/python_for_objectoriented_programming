
# Multilevel Inheritance (Kế thừa đa cấp) trong Python
# Multi-level inheritance là một lớp dẫn xuất từ một lớp dẫn xuất khác.
# Có nghĩa là một lớp cha có một lớp con và lớp con đó lại có một lớp con khác.

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
        
class FlagShip(Smartphone):    # Derived Class / Child Class
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rare_camera) # Common Method
        self.front_camera = front_camera
        
onePlus = FlagShip('OnePlus', '5', 30000, '6 GB', '64 GB', '20 MP', '16 MP')
print(onePlus.full_name())
