'''
for i in range(1,6,1):
    print(i)
else:
    print("bye")


for i in range(1,6,1):
    if i==4:
        break
    else:
        print(i)
else:
    print("bye")


for i in range(1,6,1):
    if i==4:
        continue
    else:
        print(i)
else:
    print("bye")

for i in range(1,6,1):
    if i==4:
        pass
    else:
        print(i)
else:
    print("bye")


#s = "hello world"
# index value
#h	e	l	l	o	 	w	o	r	l	d
#0	1	2	3	4	5	6	7	8	9	10

#String slicing
s = "hello world"
print(s[10])
print(s[0:5])
print(s[6:11])
print(len(s))
print(s[6: ])
#print(s[0:11:-1])
print(s[0:])
print(s[:11])
print(s[:])
print(s[::-1])
#s[start:end:decrement]

#a = "madam"
a = input("Enter a string :")
r = a[::-1]
print("Origial Value :",a)
print("Reversed Value :",r)

if a==r:
    print("Palindrome")
else:
    print("Not a palindrome")

value = input("Enter a String : ")

#find the length of an string without using pre-defined functions

length = 0
for i in value:
    length+=1
print("String Length :",length)

#find the reversed string without using pre-defined functions

reverse = ""
for i in range(length-1,-1,-1):
    reverse=reverse+value[i]
print("Reversed String :",reverse)

#check whether the string is an palindrome or not without using pre-defined functions

if value==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#pre-defined functions

s = "pyThOn ProGraMMing"

#case convertions
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())

#testing
name="Mounika"
print(name.isalpha())
numberPlate = "TN30BC6408"
print(numberPlate.isalnum())
space = " "
print(space.isspace())
passportName = "MOUNIKA"
print(passportName.isupper())
mailId="livewirenbs"
print(mailId.islower())
projectTitle = "Heart Disease Prediction Using Naive Bayes Algorithm Using Flask Framework"
print(projectTitle.istitle())
phoneNumber = "9384542020"
print(phoneNumber.isdigit())
'''

username = input("Enter the Username :")
password = input("Enter the Password :")
if username.isalpha() and len(username)>=12:
    if len(password)>=8:
        number = 0
        upper = 0
        lower = 0
        symbol = 0
        for i in password:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
            elif i.isdigit():
                number+=1
            else:
                symbol+=1
        if number>0 and upper >0 and lower>0 and symbol>0:
            print("Registered Successfully")
        else:
            print("Fill the Missing Constraint")
    else:
        print("Fill 8 characters or above")

            
else:
    print("Fill the username correctly")





















