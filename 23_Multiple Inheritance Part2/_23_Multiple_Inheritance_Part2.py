
# Multiple Inheritance Part 2

# Class con có thể thừa hưởng từ nhiều lớp cha
class A:
    def class_a_mothod(self):
        return 'I am just a class A method'
    
    def hello(self):
        return 'hello from class A'
    
class B:
    def class_b_mothod(self):
        return 'I am just a class B method'
    
    def hello(self):
        return 'hello from class B'
    
class C(A,B):
    pass

instance = C()
print(instance.class_a_mothod())
print(instance.class_b_mothod())
print(instance.hello())

# Dùng hàm help() để xem thông tin về instance
print(help(instance))

# MRO (Method Resolution Order) - Dùng để xác định thứ tự các lớp cha được kế thừa
print(C.mro())
print(C.__mro__)