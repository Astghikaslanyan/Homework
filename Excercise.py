x=13
y=156
res=x*y+1
for i in range(x,res):
	if i%x==0 and i%y==0:
		print(i)
		break

odd,even=0,0
for i in range(1,101):
	if i %2 ==0:
		even==1
	else:
		odd==1
print(odd,even)	

x,y=0,1
print(x)
while y<40:
	print(y)
	x,y=y,x+y

count_number=0
count_letter=0
string="python_3.9"
for i in string:
	if i.isalpha():
		count_letter+=1
	elif i.isdigit():
		count_number+=1
print(count_number, count_letter)

count=0
number=73421
for i in str(number):
	count+=int(i)
print(count)

n=int(input('num:'))
count=1
for i in range(2,n+1):
	count*=i
print(count)


import random
count=0
while True:
	user=int(input("num: "))
	print(count,"+",user,'=',count+user)
	count+=user

	if count>=21:
		print('You loser')
		break
	elif count == 20:
		print('21 User Win')
		break	
	elif 16<count<20:
		pc = 20 - count	
		print(count,"+",pc,'=',count+pc)
		count+=pc
	else:	
		pc=random.randint(1,3)
		print(count,"+",pc,'=',count+pc)
		count+=pc
	





