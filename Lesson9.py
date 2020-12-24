# user1=int(input("Please enter number  "))
# user2=int(input("Please enter number "))
# if user1>user2:
# 	print("user1 is greater than user2")
# elif user1<user2:
# 	print("user2 is greater than user1")
# else:
# 	print("user1 amd user2 are equal")


# number=9134
# print(str(number)[::-1])
# number1=number%10
# number2=(number%100)//10
# number3=(number%1000)//100
# number4=number//1000
# print(number1,number2,number3,number4)

# import random
# pc_point=0
# user_point=0
# while True:
# 	if pc_point>2:
# 		print('PC WINS')
# 		break
# 	elif user_point >2:
# 		print('USER WIN' )
# 		break
# 	chinga='rps'
# 	pc=random.choice(chinga)
# 	user=input("Please choose (rps) ")
# 	if pc=='r' and user=="p" or pc=='s'and user=='r' or pc=='p' and user=='s':
# 		user_point+=1
# 		print('user',user,'pc',pc,'user wins',user_point)

# 	elif pc=='p' and user=="r" or pc=='r'and user=='s' or pc=='s' and user=='p':
# 		pc_point+=1
# 		print('pc',pc, 'user',user,'pc wins',pc_point)

# 	else:
# 		print('pc',pc, 'user',user,'nobody wins')

# names=['Artur','Jon','Ani']
# for name in names:
# 	if name=='Jon':
# 	print(name)
# 		break

# names=['Artur','Jon','Ani']
# for name in names:
# 	if name=='Jon':
# 		pass
# 	else:	
# 		print(name)
# n = 12
# for x in range(2,n):
# 	if n%x==0:
# 		print('no simple')

		
# else:
# 	print("This number simple")

# color='red'
# fruits='apple'
# for x in color:
# 	for y in fruits:
# 		print(x,y)

# i=1
# while i<6:
# 	print(i)
# 	i+=1

# i=1
# while i<6:
# 	print(i)
# 	if i ==3:
# 		break
# 	i+=1

while True:
	num=input('num: ')
	if num.isdigit():
		num=int(num)+5
		print('good',num)
		break
	print('Please input number')

