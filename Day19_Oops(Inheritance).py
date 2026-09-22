'''
class Animal:
    def dog(self):
        print("Dog Can Barks")

a = Animal()
a.dog()
        
class Bird:
    def peacock(self):
        print("Birds Can Fly")
b = Bird()
b.peacock()

#single inheritance
class human1:
    def karthick(self):
        print("good player")

class human2(human1):
    def azar(self):
        print("professional player")
h2 = human2()
h2.azar()
h2.karthick()

#multiple inheritance
class Addition:
    def add(self):
        print("addition function")

class Subtraction:
    def sub(self):
        print("Subtraction function")

class Multiplication:
    def mul(self):
        print("Multiplication function")

class Division:
    def div(self):
        print("Division function")

class Calc(Addition,Subtraction,Multiplication,Division):
    def fun(self):
        pass

c = Calc()
c.add()
c.sub()
c.mul()
c.div()

#multi-level inheritance
class Food1:
    def food1(self):
        print("Pulav Ready ......")
        
class Food2(Food1):
    def add2(self):
        print("Add Some Veggies")
        print("Veg Briyani Ready ....")

class Food3(Food2):
    def add3(self):
        print("Add some chicken")
        print("Non - veg Briyani is Ready .....")

f1 = Food1()
f1.food1()

f2 = Food2()
f2.food1()
f2.add2()

f3 = Food3()
f3.food1()
f3.add2()
f3.add3()


class gp:
    def gp(self):
        print("Grand Parent Behaviour")


class p(gp):
    def p(self):
        print("Parent Behaviour")

class child(p):
    def c(self):
        print("Child Behaviour")

ob1 = gp()
ob1.gp()

ob2 = p()
ob2.gp()
ob2.p()

ob3 = child()
ob3.gp()
ob3.p()
ob3.c()
'''
#hierachical inheritance
        
class Manager(Bank):
    def managerWork(self):
        print("Managing The Team")

class CashCounterTeam(Manager):
    def CCTWork(self):
        print("Deposite / Withdraw The Cash")

class CustomerServiceTeam(Manager):
    def CSTWork(self):
        print("Handling The customer")

class LoanManagementTeam(Manager):
    def LMTWork(self):
        print("Assign the Loan")

class AccountManagementTeam(Manager):
    def AMTWork(self):
        print("Create / Delete / Manage the account")

o1 = Manager()
o1.managerWork()

o2 = CashCounterTeam()
o2.managerWork()
o2.CCTWork()

o3 = CustomerServiceTeam()
o3.managerWork()
o3.CSTWork()

o4 = LoanManagementTeam()
o4.managerWork()
o4.LMTWork()

o5 = AccountManagementTeam()
o5.managerWork()
o5.AMTWork()







