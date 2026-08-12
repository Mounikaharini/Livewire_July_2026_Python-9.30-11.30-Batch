
#without return without parameter
def add():
    a=10
    b=20
    print(a+b)
add()

#without return with parameter
def add(a,b):
    print(a+b)
add(21,25)

#with return without parameter
def add():
    a=10
    b=90
    return a+b
z = add()
print(z)

#with return with parameter
def add(m,n):
    return m+n
x = add(12,56)
print(x)

#recursion
'''
A recursive function is a function that calls itself in
order to solve a problem.
'''

def fun1():
    print("hi")
    fun1()
fun1()

def fun1():
    print("hi")
    
c=1
while c<=3:
    fun1()
    c+=1

def login():
    username = input("Enter the username : ")
    password = int(input("Enter the Password : "))
    if(username=="abc" and password==123):
        print("Login successful")
        return True
    else:
        print("Login Failed ! Try Again")
        return False 
    
c=1
while c<=3:
    if login():
        break
    c+=1

#lambda function
'''
A lambda function is a small, anonymous function (no name).
Defined using the keyword lambda.

Syntax : lambda arguments: expression
'''

square = lambda a : a * a
print(square(10))

number = lambda n : n%2==0
if number(14789)==True:
    print("Even Number")
else:
    print("Odd Number")


#Map and Filter Function

'''
map -> Applies a given function to each item of an iterable
(like a list) and returns a new iterable (map object).
Often used when you want to transform all elements.

filter -> Applies a function that returns True/False to each
item . Keeps only the items where the function returns True .
Often used when you want to select certain elements.


'''

def oe(n):
    if n%2==0:
        return True
    else:
        return False
number = [1,2,3,4,5]
print(list(map(oe,number)))
print(list(filter(oe,number)))












