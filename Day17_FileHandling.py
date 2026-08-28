'''
#---Write Mode---

f = open("newfile.txt","w")
print("File opened")
f.write("bye")
f.close()
print("Written Successfully")

#---Append Mode---

f = open("newfile1.txt","a")
print("File opened")
f.write("\nline2")
f.close()
print("Written Successfully")

#---Read Mode---

f=open("newfile1.txt","r")
print(f.read())#read all characters
print(f.read(20))
print(f.readline())
print(f.tell())
print(f.readlines())
'''

foodList = ['1.Briyani - Rs.100','2.Veg Rice - Rs.120','3.Chicken Rice - Rs.150']

def greet():
    print("          Welcome to MH Foods")
    print("-----------------------------------------")

def bill(q,ch,price):
    foodList = ['1.Briyani - Rs.100','2.Veg Rice - Rs.120','3.Chicken Rice - Rs.150']
    import time
    date = time.ctime()
    food = foodList[ch]
    bill =f"""          Welcome to MH Foods
-----------------------------------------
Date : {date}
-----------------------------------------
Ordered Food :{food}
Quantity     :{q}
Total Price  :{price*q}
-----------------------------------------
Thank You For Visiting !! Visit Again !!!
"""
    print(bill)
    f=open("bills.txt","a")
    f.write(bill)
    f.close()

    
greet()
for i in foodList:
    print(i)
ch = int(input("Enter the choice (1/2/3) :"))
q = int(input("Enter the quantity (In Numbers) :"))
if ch==1:
    bill(q,ch-1,100)

elif ch==2:
    bill(q,ch-1,120)

elif ch==3:
    bill(q,ch-1,150)

else:
    print("Invalid Choice")












