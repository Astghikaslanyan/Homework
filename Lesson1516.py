my_list= ["a", 1,2.5,(2,5), True]

computers=['ASUS', "LG", "LENOVO", 'APPLE']
user=input("Enter computer name ")
if user.upper() in computers:
	print("Yes")
else:
	print('No')

password=input("Please enter your password ")
number=0
characters=("!","@","#","$","%","&")
character=0
letter=0
if len(password)<8:
	print("Your password lenght is not 8")
else:
	for i in password:
		if i.isdigit():
			number+=1
		elif i in characters:
			character+=1
		elif i.isalpha():
			letter+=1
	if number>1 and character>1 and letter>1:
		print("Strong")
	else:
		print("Your password doesn't have number or character")

link='www.youtube.com?=hjkkjskkn'
index=0
for i in link:
	index+=1
	if i=="=":
		break
print(link[index:])		
print('id,',link[link.index('=')+1:])

word=input("Enter word ")
if word==word[::-1]:
	print("Yes")
else:
	print("closed")

mylist=[12,21,15,9,8]
newlist=[]
for i in mylist:
	if i%2==0:
		newlist.append(i)
print(newlist)

x="hello"
print(x.split())

num='5,6,a,7,b'
print(num.split(','))
work=input("hello").split()
print(work)

oldlist=[1,2,3,4,5]
oddlist=[]
for i in oldlist:
	if i%2==1:
		oddlist.append(i)
		oldlist.remove(i)
print(oddlist)
print(oldlist)


my_list=[1,2,3,6,6,8]
newlist=[]
for i in my_list:
	if i not in newlist:
		newlist.append(i)
print(newlist)
