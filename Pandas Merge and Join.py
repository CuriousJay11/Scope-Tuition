import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

print("Students DataFrame:")
print(students)

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
})

print("Marks DataFrame:")
print(marks)

result = pd.merge(students, marks, on="ID")

print(result)

#result = students.join(marks)
#print(result)

#---------------------------------------------------------------------------------------------------------


import pandas as pd

students = pd.DataFrame(
    {
        "Names": ["Manny", "Cailiuo", "Sara"]
    },
    index=[1, 2, 3]
)

marks = pd.DataFrame(
    {
        "Marks": [85, 90]
    },
    index=[1, 2 ]
)

result = students.join(marks)

print(result)

#-------------------------------------------------------------------------------------------

import pandas as pd


data = {
    "Name": ["Chez", "Nob", "Stanley", "Robert", "Eva"],
    "city": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "marks": [85, 90, 78, 88, 92],
    "age": [20, 21, 19, 22, 20]
}


df = pd.DataFrame(data)

print(df)

pivot = pd.pivot_table(df,values="marks",index="city",aggfunc="sum")

print(pivot)