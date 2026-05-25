list = ['1','2','3','4','5','6','7']
print(list[2:4])
print(list[:-2])


thislist = ['Red','Orange','Blue','Green']
if "Red" in thislist:
    print("Yes")
print(thislist[2])

#insert()
thislist.insert(2,'Black')
print(thislist)

#Append Items

#append()

thislist.append('Golden')
print(thislist)

mylist = ["Beach","Bath","Ice","Breeze"]
Tropical = ["Sunny","Icecream","Mojito","Cucumber"]

mylist.extend(Tropical)
print(mylist)

#Remove() TO remove
#-Remove item

#Pop()
#-Remove the index

mylist.remove('Beach')
print(mylist)

mylist.pop(3)
print(mylist)

mylist.clear()
print(mylist)


ToDoList = []
