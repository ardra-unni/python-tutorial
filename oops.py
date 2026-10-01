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


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def display_employee(self):
        print(f"name: {self.name}, salary: {self.__salary}")

    def add_money(self,new_amount):
        self.__salary+=new_amount

emp1=employee("john",50000)
emp1.display_employee()

emp1.add_money(5000)
emp1.display_employee()



