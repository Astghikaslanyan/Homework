a=()
b=tuple()
print(type(a))
print(type(b))
tup1=('physics', 'chemistry', 1997, 2000)
print(tup1.__sizeof__())
thistuple=('apple','banana','cherry')
if 'apple' in thistuple:
	print("Yes'apple' is in the fruits tuple")
	

thistuple=("apple", "banana", "cherry","kiwi")
# for x in thistuple:
# 	if x=="banana":
# 		pass
# 	print(x)
print(thistuple[1]) 
print(thistuple[1:2])

x=(5,10,15,20)
y=reversed(x)
print(tuple(y))
print(x[::-1])
thistuple=("apple", "banana", "cherry","oragne","kiwi","melon", "mango")
print(thistuple[-4:-1])
print(thistuple[-1])




fruits=['banana', 'apple','cheery']
fruits[1]='kiwi'
print(fruits)

fruits=['banana','apple','cherry']
fruits.append('orange')
print(fruits)

fruit=['banana', 'apple','cherry']
fruit.insert(1,'orange')
print(fruit)



fruits=['banana', 'apple', 'cherry']
fruits.pop()
print(fruits)

fruits=['banana', 'apple', 'cherry']
del fruits[2]
print(fruits)


fruits=['banana', 'apple', 'cherry']
del fruits
print(fruits)

numbers=[34,56,-456,7.56,-2.34]
numbers.sort()
print(numbers[-1])

list_my =[12,2,4,65,23]
count=0
for i in list_my:
	count+=i
print(count)