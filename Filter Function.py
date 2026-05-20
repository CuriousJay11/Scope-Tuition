#Used to extract elements for an iterable or a sequence(list,tuple) based on condition
#syntax - filter(fn,iterable)
#t returns afilter object
nos = [1,2,3,4,5,6]
def is_even(n):
    return n%2 == 0

result = filter(is_even,nos)
print(list(result))

#or

result = filter(lambda x:x%2==0,nos)
print(list(result))

#use filter() to filter names whose length > 4
names = ["Alice",'Bob','Sam','ChinnaswamyMuthaswamyShreyasIyerVenugopalan',"Vijay"]
result = filter(lambda names: len(names)>4,names)
print(list(result))

#sort() method
list2 = [1,2,3,4]
list2.sort(reverse=True)
print(list2)

#syntax ust.sort (key=lambda), (variable=conditions)
words = ["Apple","Orange",'Banana']
words.sort(key=lambda x,: len(x))
print(words)
#sorting happens according to length


students = [("Raman",85),("Aman",92),("Zoya",78)]
students.sort(key=lambda x : x[1],reverse=True)
print(students)

purchases = [("Laptop",50000),("Mouse",500),("Phone",20000)]
purchases.sort(key=lambda x : x[1],reverse=False)
print(purchases)
