#Args and Kwargs are parameters
#They are used when we dont know how many arguements will be passed to a fn

#1. *Args 
#- Allows a fn to take multile values
#- Stores args in tuple

def fn (*numbers):
    print(numbers)

fn(1,2,3,4,5,6,7,8)

def total(*numbers):
    sum = 0
    for i in numbers:
        sum+=i

    print("Total=",sum)

total (10,20,30)

#2.Kwargs-Allows multiple keyword arguements
#|-> Stores data in form of dictionary(Key:Value Pairs)

def details(**data):
    print(data)
details(name="Rachel",age=15)

#Accessing Values
def std(**info):
    print("Name:",info["name"])
    print("Marks:",info["marks"])
std (name="Zoey",marks=79)

#Using together *Args comes before **Kwargs
def show(*args,**kwargs):
    print(args)
    print(kwargs)
show(1,2,3, name ="Vijay",age="20")

