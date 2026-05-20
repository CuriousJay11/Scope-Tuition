#Map() fn
#Syntax map(function,iterable)
#Applies a fn to every element of an iterable

numbers=[1,2,3,4]
result = list(map(lambda x: x*x,numbers))
print(list(result))

#Give answer in form of list