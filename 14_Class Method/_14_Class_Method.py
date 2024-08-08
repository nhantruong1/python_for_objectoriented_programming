
class Laptop:
    discount = 10 # Class variable
    def __init__(self,name,price):
        self.name = name        # Instance attribute
        self.price = price
       
    # Class method được sử dụng để định nghĩa một phương thức thuộc về lớp chứ không phải về đối tượng của lớp
    # Phương thức này nhận tham số đầu tiên chính là lớp đó ('cls' hoặc tên khác) thay vì 'self'
    # Class method có thể thay đổi các hành vi của lớp và tất cả instance của nó
    @classmethod    # Class method
    def from_string(cls,string):
        # cls is represent the class Laptop
        import re
        item = re.findall(r'is \w*', string)
        name = item[0][3:]
        price = item[1][3:]
        return cls(name,int(price))
        
    def applydiscount(self):    # Instance method
        discountAmount = (self.price/100)*self.discount
        finalAmount = self.price - discountAmount
        return int(finalAmount)

m6600 = Laptop('m6600', 50000)
# Class method có thể được gọi qua lớp mà không cần tạo instance của lớp đó
m4800 = Laptop.from_string('my laptop is m4800 and price is 40000')
print(m4800.__dict__)