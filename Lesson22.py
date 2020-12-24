set1={12,23,'11',"hello"}
print(set1)

this_set={"apple","banana","cherry"}
for x in this_set:
	print(x)

thisset={"apple","banana","cherry"}
print("banana" in thisset)


c={1,2,3,4}
c.add(6)
print(c)

z={5,8,9}
c.update(z)
print(c)

z={5,3,9}
z.remove(3)
z.discard(8)
print(z)

set1={"a", "b","c"}
set2={1,2,3}

set3=set1.union(set2)
print(set3)

set1={12,23,"11","hello"}
set2={14,3,"141","world"}
print(set1.isdisjoint(set2))


my_string=("astghik aslanyan")
print(my_string.capitalize()) #first letter upper
print(my_string.lower()) #all letters lower
print(my_string.upper()) #all letters upper
print(my_string.title()) #all first letters in words upper 


print(ord('b'))


import random
a=[1,12,32,45,57,78,9]
	radom.shuffle(a)

import sys
x=7
print(sys.getsizeof(x))

mylist=[1,2,3,4]

mylist2=[5,6,7]


for i in mylist:
	if i in mylist2:
		print(i)
		print('yes')
		break
else:
	print('no')



