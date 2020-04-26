# Q1. How to print no. of instance.
class Person:
    count_instance=0
    def __init__(self,name,age):
        Person.count_instance +=1
        self.name=name
        self.age=age
p1=Person('Manihs',25)
p2=Person('Kumar',27)
p3=Person('Shashi',22)
print(Person.count_instance)