'''
1. if
2. if - else
3. if elif else
4. nested if

#simple if
ticket = "yes"
if ticket=="yes":
    print("Go to inside of the theatre")

#if - else
ticket = "yes"
if ticket=="yes":
    print("Go to inside of the theatre")
else:
    print("Get the ticket")

a = int(input("Enter a number :"))
if a%2==0:
    print("even")
else:
    print("odd")

b = int(input("Enter a number :"))
if b%5==0:
    print("It is a multiple of 5")
else:
    print("It is not a multiple of 5")

b = int(input("Enter a number :"))
if b%3==0 and b%5==0:
    print("It is a multiple of 5 & 3")
else:
    print("It is not a multiple of 5 & 3")

# if elif else

print("""    Payment Method
------------------------
Enter 1 for Google Pay
Enter 2 for Phonepe
Enter 3 for Amazon Pay
Enter 4 for Paytm
------------------------
""")
a = int(input("Enter the choice :"))
if a==1:
    print("Thank you for choosing Google pay")
elif a==2:
    print("Thank you for choosing Phonepe")
elif a==3:
    print("Thank you for choosing Amazon pay")
elif a==4:
    print("Thank you for choosing Paytm")
else:
    print("Invalid payment method")

#nested if

age = int(input("Enter the age :"))
voteId = input("Did you have Vote id ? Enter (yes / no) :")

if age>=18:
    if voteId=="yes":
        print("Eligible to vote")
    else:
        print("Not Eligible to vote .. Because You Don't have voter Id")
else:
    print("Not Eligible to vote .. Because you're Under 18 years")

'''
vowel = ['a','e','i','o','u']
ch = input("Enter a character :")
if ch>='a' and ch<='z':
    if ch in vowel:
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("It is not a alphabet")








