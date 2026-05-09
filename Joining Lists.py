list1= ['3']
list2=['8']
list3 = list1 + list2
print(list3)

#OR

list1.extend(list2)
print(list1)

#Print 1st
colours = ['Red','Green','Blue']
print(colours[0])

#Change 2nd item to Yellow
colours[1]="Yellow"

#Add purple to end of list
colours.append('Golden')
print(colours)

#Remove red
colours.remove('Red')
print(colours)