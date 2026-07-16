'''
syntax
------ 
variable = initial value
while variable < or > condition:
    ....
    block
    ...
    increment / decrement the variable

Algorithm for printing 1 to 10 using while loop

step 1 : choose loop
step 2 : initalization i = 1
step 3 : give the condition to end i<11 / i<=10
step 4 : inside the block print(i)
step 5 : inside the block , increase the value of i , i+=1

i = 1
while i<=10:
    print(i)
    i+=1

i = 1
while i<=10:
    print(i)
    i+=2

i = 0
while i<=10:
    print(i)
    i+=2


i = 10
while i>=1:
    print(i)
    i-=1

i = 10
while i>=1:
    print(i)
    i-=2

i = 9
while i>=1:
    print(i)
    i-=2


# * * * * *

i = 1
while i<=5:
    print('*',end=" ")
    i+=1

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

j = 1
while j<=5:
    i = 1
    while i<=5:
        print('*',end=" ")
        i+=1
    print()
    j+=1
'''
#count the digit
n = 54785435
c = 0
while n>0:
    n = n // 10
    c+=1
print(c)

#sum of digit
n = 574
s = 0 
while n>0:
    s = s + (n%10)
    n = n // 10
print(s)




