class Laptop:
    discount = 10
    sno = 0
    def __init__(self,name,price):
        Laptop.sno += 1
        self.sno = Laptop.sno
        self.name = name
        self.price = price
    def applydiscount(self):
        discount_amount = (self.price/100) * self.discount
        finalAmount = self.price - discount_amount
        return finalAmount

laptop1 = Laptop('Dell Inspiron 15', 45000)
laptop2 = Laptop('HP Pavilion', 45000)

# Add a new attribute bluetooth to the object laptop1
print(laptop1.__dict__)
laptop1.bluetooth = 'Yes'
print("After adding bluetooth attribute to laptop1:")
print(laptop1.__dict__)

# hàm applydiscount sẽ tìm xem có attribute discount trong object không, nếu không thì sẽ tìm trong class
print(laptop1.applydiscount())
laptop2.discount = 5
print(laptop2.applydiscount())

# Class variable sẽ được chia sẻ giữa các object (Nghĩa là sẽ được khởi tạo 1 lần)
# Nếu thay đổi giá trị của class variable thông qua object thì giá trị của class variable sẽ không thay đổi
print(laptop1.__dict__)
print(laptop2.__dict__)