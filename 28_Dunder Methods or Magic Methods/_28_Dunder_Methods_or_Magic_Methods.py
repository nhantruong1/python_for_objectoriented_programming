# Dunder Methods or Magic Methods
# ------------------------------------------------
# __name__    # Dunder / Magic Methods

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price, 0)
        
    # SDR method -> Sử dụng để in ra thông tin của object dành cho người dùng
    def __str__(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"
    # RPA method -> Sử dụng để in ra thông tin của object dành cho lập trình viên
    def __repr__(self):
        return f"Phone( \'{self.brand}\', \'{self.model_name}\', {self. price})"

phone1 = Phone('Nokia', '1100', 1000)
print(phone1)
print(str(phone1)) # phone1.__str__()
print(repr(phone1)) # phone1.__repr__()

# Một số các dunder methods khác mà có thể tự định nghĩa

# __len__(self) -> Dùng để trả về độ dài của object -> len(phone1)
# __del__(self) -> Dùng để xóa object -> del phone1
# __getitem__(self, index) -> Dùng để lấy giá trị của object theo index -> phone1[index]
# __setitem__(self, index, value) -> Dùng để set giá trị của object theo index -> phone1[index] = value
# __delitem__(self, index) -> Dùng để xóa giá trị của object theo index -> del phone1[index]


# __add__(self, other) -> Dùng để cộng 2 object với nhau -> phone1 + phone2
# __sub__(self, other) -> Dùng để trừ 2 object với nhau -> phone1 - phone2
# __mul__(self, other) -> Dùng để nhân 2 object với nhau -> phone1 * phone2
# __truediv__(self, other) -> Dùng để chia 2 object với nhau -> phone1 / phone2
# __floordiv__(self, other) -> Dùng để chia lấy phần nguyên 2 object với nhau -> phone1 // phone2
# __mod__(self, other) -> Dùng để chia lấy phần dư 2 object với nhau -> phone1 % phone2
# __pow__(self, other) -> Dùng để lấy lũy thừa 2 object với nhau -> phone1 ** phone2
# __and__(self, other) -> Dùng để thực hiện phép AND 2 object với nhau -> phone1 & phone2
# __or__(self, other) -> Dùng để thực hiện phép OR 2 object với nhau -> phone1 | phone2