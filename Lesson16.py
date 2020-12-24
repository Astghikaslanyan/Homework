person2={'name':"Astghik", "year":1996, "followers":500, "phone": "098356595"}
res=person2.popitem()
print(res)

year=int(input("Enter new year"))
person2['year']=year
print(person2)
person2["last_name"]="Aslanyan"
print(person2)
 person={
	'name':'Ani',
	"age":1996,
	'email':'astghik.aslanyan.1996@gmail.com'
}
for i,j in person.items():
	print(i,j)

for i in person:
	print(i)
for i in person.values():
	print(i)

person={

	"Arpi":12,
	"Astghik":1985,
	"Armo":15,
	"Ani":14,

}
age=0
for i in person.values():
	if i>age:
		age=i
print(age)
for i in person:
	if person[i]==age:
		print(i)
		break
age=sorted(person.values())[-1]
print(age)

age=sorted(person.values())[0]
for i in person:
	if person[i]==age:
		print(i)


students={

	"Arpi":12,
	"Astghik":1985,
	"Armo":15,
	"Ani":14,

}
mog=0
for i in students.values():
	mog+=i
print(mog/len(students))

students={

	"Arpi":12,
	"Astghik":1985,
	"Armo":15,
	"Ani":14,

}
for i in students:
	if students[i] > 14:
		print(i)

students={

	"Arpi":12,
	"Astghik":1985,
	"Armo":15,
	"Ani":14,

}
if "Ani" in students:
	print("yes")