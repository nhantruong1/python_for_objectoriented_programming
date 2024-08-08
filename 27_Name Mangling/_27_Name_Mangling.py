
# Name Mangling
# It is used to make attributes of a class hidden from the outside world.
# là một cơ chế trong Python được sử dụng để tránh xung đột tên trong trường hợp kế thừa đa cấp

# Name mangling là một cơ chế hữu ích trong Python để bảo vệ các thuộc tính và phương thức private khỏi sự truy cập không mong muốn và tránh xung đột tên trong kế thừa đa cấp. 
# Tuy nhiên, nó không phải là một biện pháp bảo mật hoàn toàn, mà chỉ là một biện pháp để tránh các xung đột tên và nhầm lẫn trong mã nguồn.

# Method 1: __name -> _ClassName__name
# Method 2: ClassName_name

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = max(price, 0)
        
    def __full_name(self):
        return f"{self.brand} {self.model_name}"
    
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera

    def __full_name(self):
        return "HELLO"
        
phone1 = Phone('Nokia', '1100', 1000)
smartphone1 = SmartPhone('OnePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
print(phone1.__dict__)
# print(phone1.__price) # ERROR -> because __price -> _Phone__price. Đây chính là cách bảo vệ thuộc tính private trong Python
print(phone1._Phone__price) # Nhưng vẫn có thể truy cập được thông qua cách này, vì thế nên nó chỉ dùng để tránh xung đột tên và nhầm lẫn trong mã nguồn

print(smartphone1._Phone__full_name())
print(smartphone1._SmartPhone__full_name())
# Bằng cách đặt tên method là __full_name, nó sẽ trở thành _SmartPhone__full_name và _Phone__full_name
# Nhưng vẫn có thể truy cập được thông qua cách này, vì thế nên nó chỉ dùng để tránh xung đột tên và nhầm lẫn trong mã nguồn
# Để chạy chúng ta cần chỉ rõ tên class trước method, Trong C++ thì có virtual và override để giải quyết vấn đề này