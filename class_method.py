#class method
#differnce between class method and instance method
class Laptop():
    # class variable/ class attribute
    laptop_discount=30
    count_instance=0
    def __init__(self,name,model_name,price):
        Laptop.count_instance+=1
        self.laptop_name=name
        self.laptop_model=model_name
        self.laptop_price=price
        #instance method

    @classmethod # class method
    def count_instances(cls):
            return f"you have created {cls.count_instance} of a Laptop class"

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
print(Laptop.count_instances())