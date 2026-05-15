# Python Dictionaries
#Ordered
#Changeable
#Doesnt allow duplicates


thisdict = {"brand": "Ford",
            "Model": "Mustang",
            "Year": 1967,
            "Year": 2020

            }

print(thisdict["brand"])
print(thisdict)
print(len(thisdict))

#Constructor for Dictionaries?
#- Dict()

#Accesing the items of a dictionary by reffering to its key name inside square brackets
y = thisdict["Model"]
print(y)

z = thisdict.get("Model")
print(z)

#How to get the list of all th key in key()

y = thisdict.keys()
print(y)

#Add any items
x = thisdict.keys()
print(x)
thisdict["color"] = "yellow"
print(x)

#For values print

x = thisdict.values()
print(x)
thisdict["color"] = "yellow"
print(x)

x = thisdict.items()
print(x)
#This will return each item in dictionary as tuples in list

if "model" in thisdict:
 print("yes")
else:
 print("no")

# Can you access items by using key values, True

#How to change dictionary items

thisdict["Year"] = 1862
print(thisdict)

#Update()
#It can update the dict with the items from the given arguements
#Arguement must be a dictionary with key:value pairs
thisdict.update({"Year":2020})
print(thisdict)

