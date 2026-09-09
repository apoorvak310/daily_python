# #1. Display Student name, roll no, marks
class Student:
    def __init__(self,n,rno,m):
        self.n = n
        self.rno = rno
        self.m = m
    def display_info(self):
        msg = f'Name: {self.n} Roll No.: {self.rno} Marks: {self.m}'
        return msg
s1 = Student('Rahul',101,85)
res = s1.display_info()
print(res)

#2. return area and perimeter of a rectangle
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l + self.b)
r1 = Rectangle(10,5)
area = r1.area()
perimeter = r1.perimeter()
print(area)
print(perimeter)

#3. display employee name, id and salary
class Employee:
    def __init__(self,name, e_id, sal):
        self.name = name
        self.e_id = e_id
        self.sal = sal
    def info(self):
        display = f"Name: {self.name} Employee Id: {self.e_id} Salary: {self.sal}"
        return display
    def bonus(self, b):
        new_sal = self.sal + b
        return new_sal
e1 = Employee('Arjun',101,30000)
res = e1.bonus(1000)
res2 = e1.info()
print(res2)

#4. display a mobile brand, model and price
class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def info(self):
        return f"Brand: {self.brand} Model: {self.model} Price: {self.price}"
m1 = Mobile('Samsung','A55',30000)
res = m1.info()
print(res)
