# Operator Overloading

class Phone:
    def __init__(self, brand, model, price):
        self.price = price
        self.brand = brand
        self.model = model
       
    # Operator Overloading
    def __add__(self, other): # phone1 + phone2
        return self.price + other.price
    
    def __lt__(self, other): # phone1 < phone2
        return self.price < other.price
    
phone1 = Phone('Nokia', '1100', 1000)
phone2 = Phone('Nokia', '1600', 1200)
print(phone1 + phone2)
print(phone1 < phone2)
print(phone1.__dict__)