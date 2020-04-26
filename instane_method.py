# instance method
class Pesron:
    def __init__(self,fisrt_name,last_name,age):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.age=age
    def full_name(self): #instane method
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

p1=Pesron('Manish','Kuamr',25)
print(p1.first_name)
print(p1.last_name)
print(p1.full_name())
print(p1.is_above_18())



# Q1. create a laptop class with attributes like brand name, model name, price. create two objects/instance of your laptop class. and discount the laptop price.
class Laptop():
    def __init__(self,name,model_name,price):
        self.laptop_name=name
        self.laptop_model=model_name
        self.laptop_price=price
        #instance method
    def apply_discount(self,num):
        off_price= (num/100)*self.laptop_price
        return self.laptop_price-off_price

laptop1=Laptop('HP','15-ac40TU',60000)
laptop2=Laptop('Dell','15-ac43TU',60000)
print(laptop1.laptop_name,"",laptop1.laptop_model,"",laptop1.laptop_price)
print(laptop2.laptop_name,"",laptop2.laptop_model,"",laptop2.laptop_price)
print(laptop1.apply_discount(50))
print(laptop2.apply_discount(30))