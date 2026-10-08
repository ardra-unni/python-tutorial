# class car:
#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price

#     def display_info(self):
#         print(f"car: {self.make} {self.model} {self.year} {self.price}")

# car1=car("honda","civic",2022,5000000)
# car1.display_info()
# car2=car("ford","mustang",2001,7000000)
# print(car1)

# #accessing object attributes
# print(car1.price)


# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary

#     def display_employee(self):
#         print(f"name: {self.name}, salary: {self.__salary}")

#     def add_money(self,new_amount):
#         self.__salary+=new_amount

# emp1=employee("john",50000)
# emp1.display_employee()

# emp1.add_money(5000)
# emp1.display_employee()

# class animal:
#     def speak(self):
#         print("make a sound")

# class dog(animal):
#     pass

# dig1=dog()
# dig1.speak()

class dog:
    def sound():
        print("bark")

class cat:
    def sound():
        print("meow")

dog=dog
cat=cat
dog.sound()
cat.sound()

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

    def area1(self):
            return self.width * self.height

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius  * self.radius

a=rectangle(10,20)
print(a.area1())
    
b=circle(6)
print(b.area())




