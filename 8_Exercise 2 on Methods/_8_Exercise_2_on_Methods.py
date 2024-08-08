class Product:
    def __init__(self,productName,price):
        self.productName = productName
        self.price = price
    def discount(self,discountValue):
        discountAmount = (self.price/100) * discountValue
        finalPrice = self.price - discountAmount
        return int(finalPrice)

laptop = Product('Dell Inspiron 15', 45000)
print(laptop.discount(10))