Sets = {"Red","Brown","Pink"}
print(Sets)

#Unordered,UnchangeableUnindexed

Colours = {"Green","Red","Brown",True,False,1,0}
print(Colours)


#Add() Method
x ={"Red","Green","Blue"}
x.add("Orange")
print(x)

print("Green" in x)

#Remove()/Discard() Method

#To delete the set delete()

#del -> Keyword
#del x
#print(x)

#Difference bewteen Del and Clear

# Del is keyword, Clear is a function with round brackets

thisset = {"Apple","Orange","Banana"}
for x in thisset:
 print(x)

#Join 2 or more sets
#Union() and Update() - All the items from both sets
#Intersection Method - Duplicates
#Difference() - Keeps items from first set that are not in other sets
#Symmetrical Difference() - Method keeps all items EXCEPT duplicates

set1 ={"Benz","Bayerishche Motern Werke","Kia","Infinity"}
set2 = {1,2,3,4}
set3 = {"Google","Opera","Safari",3}
set4 = {"Hyundai","Lexus","Infinity","Benz"}

myset = set1.union(set2,set3,set4)
print(myset)
             #OR

myset = set1|set2|set3|set4
print(myset)

myset = set1.intersection(set4)
print(myset)

#Intersection_Update Method

set1.intersection_update(set4)
print(set1)

#Difference

myset = set2.difference(set3)
print(myset)

#Can sets join with other data types
z = {"Red","Green","Blue"}
y = ("Yellow","Pink","Black")

w = z.union(y)
print(w)

# Difference_Update, Method to keep only items from the first set that are not present in the other sets

set2.difference_update(set3)
print(set2)

#Symmetric_Difference() - method will not print the common items
# Can also use ^ operator (Power)


Number = {1,2,3,4,"Google"}
SearchEngines = {"Google","Opera","Safari",3,1}

V = Number.symmetric_difference(SearchEngines)
print(V)
