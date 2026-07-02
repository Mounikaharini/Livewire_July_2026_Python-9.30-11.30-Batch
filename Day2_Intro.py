#data types
'''
a = 10
print(a)
print(type(a))

a = 10.09
print(a)
print(type(a))

a = True
print(a)
print(type(a))

a = [1,1,2.0,2.0,'a',"hello",[1,2,3]]
print(a)
print(type(a))

a = (1,1,2.0,2.0,'a',"hello",[1,2,3])
print(a)
print(type(a))

a = {1,1,2.0,2.0,'a',"hello"}
print(a)
print(type(a))

a = {1:"amazon app",2:"flipkart app",1:"meesho app"}
print(a) 
print(type(a))

#arithmetic operators

a = 11
b = 2
print(20+20)
print(20+a)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#assignment operator

x=10

x=x+10
x=10+10
x=20

print(x)
x+=20

x=x+20
x=10+20
x=30

print(x)
x-=20
print(x)
x*=2
print(x)
x/=5
print(x)
x//=2
print(int(x))
x%=1
print(x)

#comparision operator

m = 10
n = 20
print(m==n)
print(m!=n)
print(m>n)
print(m>10)
print(m<n)
print(m<10)
print(m>=10)
print(m<=10)

#logical operator
#and / or / not

a = 18
b = 19
print(a>=18 and b>=18)

c = 16
d = 18
print(c>=18 or d>=18)

e = 10
print(not e>=10)

#and truth table
cond1	cond2	o/p
		
TRUE	TRUE	TRUE
TRUE	FALSE	FALSE
FALSE	TRUE	FALSE
FALSE	FALSE	FALSE
		
#or truth table		
cond1	cond2	o/p
		
TRUE	TRUE	TRUE
TRUE	FALSE	TRUE
FALSE	TRUE	TRUE
FALSE	FALSE	FALSE
		
#not truth table		
cond	o/p	
		
TRUE	FALSE	
FALSE	TRUE	
'''

#bitwise operator

#membership operator
# in / not in

a = [1,2,3,4,5,6,7]
print(6 in a)
print(9 in a)

print(9 not in a)
print(6 not in a)

#identity operator
#is / is not
x = 10
y = 10
print(x is y)
z = 11
print(x is z)

print(x is not z)
print(x is not y)

