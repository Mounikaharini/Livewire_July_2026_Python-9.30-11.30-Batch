
for i in range(1,5,1):
    print(i)

1
2
3

for i in range(5,0,-2):
    print(i)

5
3
1

for j in range(1,5,1):
    for i in range(1,5,1):
        print("*",end=" ")
    print()

* * * * 
* * * * 
* * * * 
* * * *

for j in range(1,6,1):
    for i in range(1,6,1):
        print(j,end=" ")
    print()

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5

for j in range(1,6,1):
    for i in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

* * * * * 
*       * 
*       * 
*       * 
* * * * *

for j in range(1,6,1):
    for i in range(1,6,1):
        if j==3 or (j==1 and i==3) or (j==2 and i==4)or(j==4 and i==4) or (j==5 and i==3):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

    *     
      *   
* * * * * 
      *   
    *
    
for j in range(1,6,1):
    for i in range(1,6,1):
        if j==3 or (j==1 and i==3) or (j==2 and i==2)or(j==4 and i==2) or (j==5 and i==3):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

    *     
  *       
* * * * * 
  *       
    *
    
a = "MOUNIKA"
for j in range(5):
    for i in a:
        print(i,end=" ")
    print()

M O U N I K A 
M O U N I K A 
M O U N I K A 
M O U N I K A 
M O U N I K A

n = int(input("Enter a value :"))
for i in range(0,n,1):
    for j in range(0,n,1):
        print(chr(65+j),end=" ")
        #for small letters -> print(chr(97+j),end=" ")
    print()

Enter a value :5
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E

n = int(input("Enter a value :"))
for i in range(0,n,1):
    for j in range(0,n,1):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(chr(65+j),end=" ")
        else:
            print(' ',end=" ")
    print()

Enter a value :5
A B C D E 
A       E 
A       E 
A       E 
A B C D E

#n = int(input("Enter a value :"))
n=5
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print('*',end=" ")
    print()

* 
* * 
* * * 
* * * * 
* * * * *

n=5
for i in range(0,n,1):
    for j in range(0,n,1):
        if i+j<=n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

* * * * * 
* * * *   
* * *     
* *       
*  



