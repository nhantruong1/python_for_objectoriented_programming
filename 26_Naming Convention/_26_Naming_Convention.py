# Naming Convention
# ------------------------------------------------
# In Python Language, EveryThing is public.
# How to define private variables and private method in Python?
# _name    # Private
# __name    # Highly Private
# __name__    # Dunder / Magic Methods
# This is just a convention.

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # Private Variable
        self._price = max(price, 0)
        
phone1 = Phone('Nokia', '1100', 1000)
