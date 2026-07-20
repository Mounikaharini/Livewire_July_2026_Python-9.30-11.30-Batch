'''
7.Write a program to print all the numbers which are
multiples of either 2 or 3 till N.

Input : 15 , Output : 2 3 4 6 8 9 10 12 14 15

n=int(input("Enter a number :"))
for i in range(2,n+1):
    if i%2==0 or i%3==0:
        print(i)
n = 20
6 12 18

#armstrong number
n = 152
n1 = n
n2 = n
c = 0
while n>0:
    n=n//10
    c+=1

s = 0
while n1>0:
    r = n1 % 10
    s = s + (r**c)
    n1 = n1//10
    
if n2==s:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

#linear search
a=[81,25,42,73,442,98,670,54,22,17,94]

key = 98

for i in a:
    if i == key :
'''
#FIND THE LARGEST ELEMENT
a=[81,25,42,73,552,98,551,54,22,17,554]

temp = 0

for i in a:
    if i>temp: #i<temp -> smallest element
        temp = i
print(temp)












