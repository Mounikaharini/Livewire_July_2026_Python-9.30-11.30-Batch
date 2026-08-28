'''
try:
    a=[2,46,8,4]
    print(a[8])
    a={'name':'kio','Age':21}
    print(a['mark'])
    n = int(input('Enter a number:'))
    print(n)
    a = 20
    print(b)

except NameError as e:
    print(e)

except ValueError as v:
    print(v)

except KeyError as k:
    print(k)

except Exception as l:
    print(l)

finally:
    print("Hi im finally")

'''
#assert -> Assertion Error
#raise  -> Raise all the types of error

'''

a=10
b=50
c=a+b
assert c==30,"Hi I'm Error"
print(c)


'''

a = 10
b = 0
if b==0:
    raise ZeroDivisionError("B value is Zero")
else:
    print(a/b)
















