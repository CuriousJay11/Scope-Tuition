import numpy as np

students = np.array(["Alex", "Rio", "Manny", "Leo"])
marks = np.array([85, 92, 78, 65])

print("Students:", students)
print("Marks:", marks)

print("\nTotal Marks:", np.sum(marks))

#Topper
topper_index = np.argmax(marks)
print("Topper:",students[topper_index])
print("In std score above 70")
print(students[marks>70])

low_index = np.argmin(marks)
print("Lowest Score:",students[low_index])
print("\n sorted marks:")
print(np.sort(marks))

print("\n Pass/Fail")
for i in range(len(students)):
    if marks[i]>=40:
        print(students[i],"Pass")
    else:
        print(students[i],"Fail")

print("\n Grades")
for i in range(len(students)):
    if marks[i]>=90:
        grade = 'A'
    elif marks[i]>= 75:
        grade = 'B'
    elif marks[i]>= 50:
        grade = 'C'
    else:
        grade = 'F'

    print(students[i],":",grade)