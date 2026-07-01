import pandas as pd

data = {"Name":["Vijay",'Chezhiyan','Rayyan','Neil'],
        'Marks':[90,85,95,88],
        "City":["Chennai","Chennai","Dubai","Toronto"]
        }

df = pd.DataFrame(data)

df.to_csv("students.csv",index=False)

print("CSV FILE SAVED!")

# Read or import that stored csv file

df = pd.read_csv('students.csv')
print(df)

#group = df.groupby("Marks")
#print(group.mean())

import pandas as pd

sales = {
    "city": [
        "New York","Los Angeles","Chicago","New York","Chicago","Los Angeles"
    ],

    "sales": [
        100,200,150,300,250,100
    ]
}

df = pd.DataFrame(sales)

print(df.groupby("city")["sales"].sum())

