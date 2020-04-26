# class:- classs is blueprint that defines complete nature of future object.
#create a class-
class Person:
    # define the attribute of a person
    def __init__(self,name,age,height): # constructor
        # self represent the own object
        # instance variable with the help of attribute
        self.name=name
        self.age=age
        self.height=height
# create an object:
# object:- an object is member of an "instance" of a class.
p1=Person('Manish', 25, 5.6)
print(p1)
print(p1.name)
print(p1.age)
print(p1.height)

# Q1. create a laptop class with attributes like brand name, model name, price. create two objects/instance of your laptop class.
class Laptop():
    def __init__(self,name,model_name,price):
        self.laptop_name=name
        self.laptop_model=model_name
        self.laptop_price=price
laptop1=Laptop('HP','15-ac40TU',60000)
laptop2=Laptop('Dell','15-ac43TU',60000)
print(laptop1.laptop_name,"",laptop1.laptop_model,"",laptop1.laptop_price)
print(laptop2.laptop_name,"",laptop2.laptop_model,"",laptop2.laptop_price)