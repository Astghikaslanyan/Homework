
import math
print(math.pi)
print(math.sqrt(16))

import random
print(random.randint(0,10))

import random
x='abcd1123456789efgh'
print(random.choice(x))

import random
x='abcd1123456789efgh'
n1=(random.choice(x))
n2=(random.choice(x))
n3=(random.choice(x))
n4=(random.choice(x))
n5=(random.choice(x))
n6=(random.choice(x))
password = (n1+n2+n3+n4+n5+n6)
print(password)
import random as r
print(r.randrange(0,100,5))
 
import time
print('hello world')
time.sleep(3)
print('bye')

import os
print(os.getcwd())

import calendar
y=int(input("Input the year:"))
m=int(input("Input the month:"))
print(calendar.month(y,m))


import datetime
x=datetime.datetime.now()
print(x)
print(datetime.date.today())

import datetime
x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime
x=datetime.datetime.now()
h=int(input("How old are you?"))
res=x.year-h
print(res)

x=4
res= x<5 and x>10
print(res)

x=4
res= x<5 or x>10
print(res)

x=4
res=not(x<5 and x>10)
print(res)

x="a"
print(id(x))
y = 'a'
print(id(y))

print(x is y)


name="aram"
print('a' in name)


question = input("Which is the best Car?")

res= "Bmw" in question
print(res)


cars="bmw audi mercedes "
car=input("what car do you want t buy? ")
print(car in cars)


import random 
x=random.randint(0,10)
y=random.randint(9,13)
print(x,y,x>y)

question=input("Do you have a iphone")=='y'

question2=input("Do you have a iphone X?")=='y'

print(question and question2)

apple=input("Do you have apple in fridge? ")=="y"
banana=input("Do you have apple in fridge? ")=="y"

light=input("do you have light at home? ")=='y'
print(apple and not light)

print("go to the shop and buy banana," ,not banana)
print("go to the shop and buy apple", not apple)



