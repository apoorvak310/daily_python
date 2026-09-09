#1. 
lst = [2, 4, 6, 8, 10]
output = list(map(lambda n:n**2,lst))
print(output)

#2.
x = [10, 15, 20, 30, 45, 50, 60, 72]
output = list(filter(lambda n: n%3 == 0 and n%5 == 0, x))
print(output)

#3.
from functools import reduce
x = [2, 3, 4, 5]
output = reduce(lambda n,m:n*m,x)
print(output)

#4.
x = [1, 2, 3, 4, 5, 6, 7, 8]
even = list(filter(lambda n:n%2 == 0, x))
output = list(map(lambda i:i**3, even))
print(output)

#5.
class Student:
    def __init__(self,n,m):
        self.name = n
        self.marks = m
    def info_display(self):
        msg = f'Name : {self.name} Marks : {self.marks}'
        return msg
obj1 = Student('rahul',85)
res = obj1.info_display()
print(res)
