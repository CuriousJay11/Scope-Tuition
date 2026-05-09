mytuple = ("red",'blue','green',"orange")
print (mytuple)

#ordered,unchangeable,allow duplicate values
#we cannot add/remove items after the creation of the tuple

print(len(mytuple))
#Creating tuple of one item
tuple1 = ('apple',)
print(tuple1)
#For type
print(type(mytuple))

#tuple() Constructor

tuple1 = tuple(("Apple","Orange",'Banana'))
print(tuple1)

#Accesing tuple items

print(tuple1[1])

#Range

print(tuple1[1:])

#Checking if value is there in tuple
if "red" in mytuple:
    print("Yes")

#How can u change the tuple values
#Tuple-Immutable
#But you can convert tuple -> list and then make changes then covert list -> tuple

x = ("BMW","BENZ",'VOLVO')
y = list(x)
y[1]="Toyota"
x = tuple(y)
print(x)

#Adding items
#|-> Convert to list
x = ("BMW","BENZ",'VOLVO')
y = list(x)
y.append("Toyota")
x = tuple(y)
print(x)

#Add tuple to tuple

x = ("BMW","BENZ",'VOLVO')
y = ("Honda","Hyundai","Maruti")
x += y
print(x)

#Remove items
#Tuple-Immutable
#But you can convert tuple -> list and then make changes then covert list -> tuple


x = ("BMW","BENZ",'VOLVO')
y = list(x)
y.remove("BENZ")
x = tuple(y)
print(x)

#Experiment,Deleted x so when u print error

#x = ("BMW","BENZ",'VOLVO')
#y = list(x)
#y.remove("BENZ")
#x = tuple(y)
#del(x)
#print(x)

#Python - Unpack Tuples
# Creating a tuple - Packing a tuple
#Its when you extract variables





#Loop in a tuple
Sports = ('Basketball','Football','Tennis')
for x in Sports:
  print(x)

#Loop through index numbers

Sports = ('Basketball','Football','Tennis')
for i in range(len(Sports)):
   print(Sports[i])

#While Loop


wtuple = ['Red','Orange','Blue','Green']
i = 0
while i < len(wtuple):
    print(wtuple[i])
    i = i+1

#Multiply tuple numerious times

wtuple = ['Red','Orange','Blue','Green']
y = wtuple * 3
print(y)
