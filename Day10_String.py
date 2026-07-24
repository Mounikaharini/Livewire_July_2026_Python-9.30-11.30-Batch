'''
#alignment and padding
a = "hi"
print(a.center(10))
print(a.ljust(10))
print(a.rjust(10))
print("52396".zfill(10))

#trimming the whitespace
b = "       hi hello    hi    "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

#split and join
c = "welcome to the python class"
print(c.split())
print(c.split(','))
d = c.split()
print(d)
print(''.join(d))
print('-'.join(d))
print(c.rsplit(' ',2))
print(c.partition('to'))

#search and replace

e = "python programming language"
print(e.find('o'))
print(e.rfind('o'))
print(e.find('z'))
print(e.index('p'))
#print(e.index('z'))
print(e.replace('a','-'))
print("26-1211".startswith('26'))
print("mounika@gmail.com".endswith('@gmail.com'))
print(e.count('g'))
'''
#string formatting

name = "Mounika"
course = "Python"
time = "9.30 - 11.30"
print("Name :",name,"\nCourse :",course,"\nTime :",time)

#F-string

print(f"Name :{name} \nCourse : {course} \nTime : {time}")
print(f"My name is {name}, I'm Currently doing {course} Course in Livewire")
mark = 62
print(f"My mark is {mark + 78}")

#str.format()
name = "Mounika"
course = "Python Full Stack"
print("My name is {}, I'm Currently doing {} Course in Livewire".format(name,course))
print("My name is {1}, I'm Currently doing {0} Course in Livewire".format(course,name))
print("My name is {n}, I'm Currently doing {c} Course in Livewire".format(c=course,n=name))

#% formatting
'''
%s - string
%d - number (integer)
%f - float
'''

print("My name is %s, I'm Currently doing %s Course in Livewire"%(name,course))

duration = 60.975767

print("My name is %s, I'm Currently doing %s Course in Livewire , The Course duration is %d Hours"%(name,course,duration))

print("Duration : %.3f"%(duration))








