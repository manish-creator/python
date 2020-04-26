class Circle:
    pi =3.14 #class variable
    def __init__(self,radius):
        self.radius=radius
    def cir_curferrance(self):
        return 2*Circle.pi*self.radius
c=Circle(4)
print(c.cir_curferrance())

# Q1. create a laptop class with attributes like brand name, model name, price. create two objects/instance of your laptop class. and discount the laptop price by using class variable.
class Laptop():
    # class variable/ class attribute
    laptop_discount=30
    def __init__(self,name,model_name,price):
        self.laptop_name=name
        self.laptop_model=model_name
        self.laptop_price=price
        #instance method
    def apply_discount(self):
        off_price= (Laptop.laptop_discount/100)*self.laptop_price
        return self.laptop_price-off_price

laptop1=Laptop('HP','15-ac40TU',60000)
laptop2=Laptop('Dell','43TU',70000)
print(laptop1.laptop_name,"",laptop1.laptop_model,"",laptop1.laptop_price)
print(laptop2.laptop_name,"",laptop2.laptop_model,"",laptop2.laptop_price)
print(laptop1.apply_discount())
print(laptop2.apply_discount())
print(laptop1.__dict__)


