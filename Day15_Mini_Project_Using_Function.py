def greet():
    print()
    print("~~          Welcome to ValidBot          ~~")
    print()
def validator():
    print("============================================")
    print("               Choose the sum")
    print("============================================",end="\n\n")
    sums = ["1.Odd or Even","2.Positive or Negative","3.Vowels or Consonants","4.Count the digits","5.Sum of Digits"]
    
    for i in sums:
        print(i)
    print()
    print("============================================")
    choice = int(input("Enter the Choice (1/2/3/4/5/(for exit 0)) : "))
    print("============================================")
    checkChoice(choice)

def checkChoice(choice):
    if choice==0:
        return
    elif choice==1:
        oddOrEven()
    elif choice==2:
        postiveOrNegative()
    elif choice==3:
        vowelsOrConsonants()
    elif choice==4:
        countTheDigits()
    elif choice==5:
        SumOfDigits()
    else:
        print("Invalid Option ! Try Again")
        validator()

def oddOrEven():
    n=int(input("Enter the number : "))
    print("--------------------------------------------")
    print("Your Answer",end=" ")
    if n%2==0:
        print(n,"is Even Number")
    else:
        print(n," is Odd Number")
        print("--------------------------------------------")
    validator()
greet()
validator()

