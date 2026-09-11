#1. Create a BankAccount class with a private variable balance. Create methods: deposit(amount) withdraw(amount) displaybalance()
class BankAccount:
    def __init__(self,bal):
        self.__bal = bal
    def getmny(self):
        return self.__bal
    def withdraw(self, mny):
        if mny <= self.__bal:
            self.__bal = self.__bal - mny
        else:
            return "Insufficient balance"
        return self.__bal
    def deposit(self, mny):
        if mny > 0:
            self.__bal = self.__bal + mny
            return self.__bal
    def check_bal(self):
        c = self.getmny()
        print("available balance is : ",end=" ")
        return c
b1 = BankAccount(10000)
print(b1.check_bal())
print(b1.withdraw(5000))
print(b1.check_bal())
print(b1.deposit(2000))
print(b1.check_bal())

#2. Create an Employee class with a private variable salary. Create: setsalary(salary) getsalary() The salary should be changed only through setsalary().
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.__sal = sal
    def get_salary(self):
        return self.__sal
    def set_salary(self, mny):
        if mny > 0:
            self.__sal += mny
            return self.__sal
e1 = Employee('Arjun', 30000)
print(e1.get_salary())
print(e1.set_salary(30000))

#3. Create a User class with private variables username and password. Create methods: login(username, password) that returns True if the username and password match, otherwise returns False.
class User:
    def __init__(self,usrname,pwd):
        self.username = usrname
        self.password = pwd
    def login(self,u,p):
        if u == self.username and p == self.password:
            return "Login successful"
        else:
   
         return False
obj = User('Arjun','1234')
print(obj.login('Arjun','1234'))


#4. Create a Temperature class with a private variable temp. Create methods: get_temp() and set_temp(temp).
class Temperature:
    def __init__(self, temp):
        self.__temp = temp
    def get_temp(self):
        return self.__temp
    def set_temp(self, t):
        if t > -273.15:
            self.__temp = t
            return self.__temp
t = Temperature(25)
print(t.get_temp())
t.set_temp(30)
print(t.get_temp())
