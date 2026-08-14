'''
import random as r

print(r.random())
print(r.randint(1,10))
print(r.randrange(0,100,5))

a = r.randrange(1000,9999)
print(a)
otp=int(input("Enter the otp : "))
if a==otp:
    print("OK")
else:
    print("No")

import sys as s

#sys.exit(0)
#print(dir(sys))
print(s.version)
print(s.path)

import socket as s
print(s.gethostname())

import pywhatkit
pywhatkit.search("livewire")

import webbrowser
webbrowser.open_new_tab("https://wayground.com/explore/admin?source=auto-trial-start")

import calendar as c
print(c.month(2026,8))
print(c.isleap(2400))
print(c.calendar(2025))

import time
print("hi")
time.sleep(2)
print('bye')
print(time.ctime())
print(time.daylight)

import datetime as d
print(d.datetime.now())

import turtle
star = turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()
'''
'''

import turtle
t = turtle.Turtle() # Create turtle object
for i in range(4):
    t.forward(100) # Move forward
    t.right(90) # Turn 90 degrees
turtle.done()

#Draw a circle
'''
import turtle
t = turtle.Turtle()
t.color("blue")
t.circle(80)
turtle.done()

