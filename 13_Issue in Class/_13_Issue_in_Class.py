class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # check is price Positive
        # Method 1:
        # self.price = price if price > 0 else 0
        # Method 2:
        self.price = max(price, 0)
        
        # Do not use this because it dont update the price if we change the price
        # self.completeSpecification = f"{self.brand} {self.model_name} and price is {self.price}"

    # Use property decorator to make a method as a attribute
    @property
    def completeSpecification(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
        
    def full_nume(self):
        return f"{self.brand} {self.model_name}"
    
phone1 = Phone('Nokia', '1100', 5000)
phone1.price = 7000
print(phone1.completeSpecification)
        