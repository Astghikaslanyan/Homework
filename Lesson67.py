question=input("What is your name? \na) 303 b) 405 \nc) 301 d) 500  --") == 'c'
print(question)
question2=int(input("When was the Avarair war? \n300  405  \n 401 800 --")) == 405
print(question2)
question3= float(input("What is the amount of pi?  \n 54.1   13.1 \n3.14 3.1 --" ))==3.14
print(question3)

age=int(input("How old are you?"))
res=17<age<25
print(res)

car="mercedes, audi, bmw"
dream_car=input("What car do you want? ")
res=(dream_car in car)
print(res)

a=27
b=14
if a>b:
	print('a is big')	

a=14
b=14
if b>a:
	print('b is big')
elif a>b:
	print("a is big")
else:
	print('a = b')

a=34
b=14
c=12
d=27
if a>b and d>c:
	print('a and d are bigger')

dog_age=int(input("How old is dog?"))
if dog_age<0:
	print("Error")
elif dog_age == 0:
	print("Human age is 0")
elif dog_age <= 2:
	print(dog_age * 5.25)
else:
	res=10.5+(dog_age-2)*4
	print(res)

vowel="aeouiy"
letter=input("The letter ")
res=letter in vowel
if res:
	print("your letter is vowel")
else:
	print("your letter is consonant")
	

vowel="aeouiy"
letter=input("The letter ")
if letter.isalpha():
	if letter in vowel:
		print("your letter is vowel")
	else:
		print("your letter is consosnat")
else:
	print("please input letter")

number=int(input("Please enter the number"))
if number%2 == 0:
	print(number,"even")
else:
	print(number,"odd")