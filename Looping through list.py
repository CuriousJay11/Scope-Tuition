Tropical = ["Sunny","Icecream","Mojito","Cucumber"]
for i in Tropical:
    print("Summer")

for i in range(len(Tropical)):
    print(Tropical[i])

thislist = ['Red','Orange','Blue','Green']
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

Tropical = ["Sunny","Icecream","Mojito","Cucumber"]

[print(x)for x in Tropical]

#Sort()

thislist.sort()
print(thislist)

list2 = ['1','5','2','6']
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list3 = list2.copy()
print(list3)

list3 = list(list2)
print(list3)



