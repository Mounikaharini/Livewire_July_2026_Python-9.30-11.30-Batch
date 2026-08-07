
'''
#reverse a number & check palindrome
a = "mom"
b = ""
l = 0
for i in a:
    l+=1
for i in range(l-1,-1,-1):
    b = b + a[i]
print(b)

if(a==b):
    print("palindrome")
else:
    print("not a palindrome")

#count lower and upper cases
a = "PyTHOn"
upper = 0
lower = 0
for i in a:
    if(ord(i)>=65 and ord(i)<=90):
        upper+=1
    elif(ord(i)>=97 and ord(i)<=122):
        lower+=1
print("Upper :",upper)
print("Lower :",lower)

#remove spaces in a string
a = "hello       world       !"

for i in a:
    if(i!=" "):
        print(i,end="")
     

def add():
    a=10
    b=20
    print(a+b)
add()

#global variable
x = 10
def a():
    print(x)
a()
print(x)

#local variable
y = 198
def b():
    print(y)
    global v
    v = 90
    print(v)
b()
print(y)
print(v)

a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

def addition(x,y): #parameter
    print(x+y)
addition(a,b) #argument

def subtraction(x,y):
    return x-y #returning a value

a = subtraction(2,7)
print(a)
'''

#TYpes of argument in a  function

#positional argument
#-> The values are passed in the same order*as the parameters are defined.

def fun1(a,b,c):
    print(a+b+c)
fun1(1,1,1)

#default argument
#->These have a default value.If no value is passed for
#that parameter, Python uses the default.
     
def fun2(name="4sf8rf"):
    print(f"Welcome {name}")
fun2()
fun2("mounika")

#keyword argument
#->Here, the parameters are specified by name while calling the function.
#Order doesn’t matter when using keywords.

def fun3(city,state):
    print(f"This is {city} city of {state} State")
fun3("salem","TN")
fun3("TN","salem")
fun3(state="TN",city="salem")

#variable length argument
'''
There are two types:
*args → Non-keyword variable arguments
**kwargs → Keyword variable arguments

# (a) Using *args
Used when you don’t know how many positional arguments will be passed.

# (b) Using **kwargs
Used when you don’t know how many keyword arguments will be passed.
''' 
#Non-keyword variable arguments

def fun4(*a):
    t = 0
    for i in a:
        t = t + i
    print(t)
fun4(1,2,3,4,5,6)

#keyword variable arguments

def fun5(**b):
    for i in b:
        print(i," : ",b[i])
fun5(name="mounika",course="python")




