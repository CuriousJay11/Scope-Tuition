import pandas as pd

data = {"name":["axel",'rio'],
        'marks':[90,85]
        }

df= pd.DataFrame(data)
print(df)

import pandas as pd
s = pd.Series([2,4,6,8,10])
print(s)


import pandas as pd

data = {"cars":["bmw",'ford','volvo'],
        'times seen in highway':[3,7,2]
        }

df= pd.DataFrame(data)
print(df.head())

import pandas as pd
a = [1,7,2]
b = pd.Series(a)
print(b)

c = pd.Series(a,index=['x','y','z'])
print(c)
print(c['z'])

import pandas as pd

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

a = pd.Series(calories, index=["day1", "day2"])

print(a)

import pandas as pd

data = {"Name":["Vijay",'Chezhiyan','Rayyan'],
        'Marks':[99,96,78],
        "City":["Chennai","Bangalore","Dubai"]
        }

df= pd.DataFrame(data)
print(df.loc[0])
print(df[df["Marks"]>80])
df['result']=['pass','pass','fail']
print(df)
print(df['Marks'].mean())

import pandas as pd

data = {"Calories":[420,380,390],
        'Duration':[50,40,45],
        }

df= pd.DataFrame(data,index=["day1",'day2','day3'])
print(df)

#ff=pd.read_csv('data.csv')
#print(ff)

#Filteration

#print(df.head()) Shows first row

#print(df.columns) Shows columns

#print(df.shape)

#print(df.head(2))
#|
#- First 2 rows

data = {"Product":["Laptop",'Mouse','Keyboard','Monitor'],
        'Price':[50000,500,1500,12000],
        "Warranty":[3,1,1,3]
        }

sf= pd.DataFrame(data)
print(sf.head())
print(sf.columns)
print(sf.shape)
print(sf.head(2))

import pandas as pd

data = {"Name":["Vijay",'Chezhiyan','Rayyan','Neil'],
        'Marks':[90,85,95,88],
        "City":["Chennai","Bangalore","Dubai","Toronto"]
        }

dataf= pd.DataFrame(data)
print(dataf[dataf["Marks"]>88])  #Shows names and marksa of student who got higher than 88

#Only names
print(dataf['Name'])

dataf['result']=['pass','fail','pass','fail']
print(dataf)  #Adding results section for pass/fail

print(dataf['Marks'].mean()) #Average Marks

#How to delete column

dataf.drop("City",axis=1)
print(dataf)


data = {"Product":["Laptop",'Mouse','Keyboard','Monitor'],
        'Price':[50000,500,1500,12000],
        "Warranty":[3,1,1,3],
        "Stock":[10,12,7,9]
        }

df= pd.DataFrame(data)
print(df)

df.drop("Stock",axis=1,inplace=True)  #Deleting Column , Column axis = 1, Row axis= 0 
print(df)

#----------------------------------------------------------------------------------------------------------

data = {
    "City": ["Delhi", "Dehli", "Mumbai", "Mumbai"],
    "Sales": [200000, 400000, 100000, 700000],

}

df= pd.DataFrame(data)
print(df)

#pivot = pd.pivot_table(df,values="Sales",index="City",aggfunc=["sum","mean","max"])
#print(pivot)

#-------------------------------------------------------------------------------------------------------------

#Missing DATA value

import numpy as np

data = {"Name":["Vijay",'Chezhiyan','Rayyan','Neil'],
        'Marks':[90,np.nan,95,np.nan],
        "City":[np.nan,"Bangalore",np.nan,"Toronto"]
        }

df= pd.DataFrame(data)
print(df)

#Counting Missing VALUES

print(df.isnull().sum())

#DETECT IF ANY MISSING VALUES

print(df.dropna())

print(df.isnull()) # Checks missing values and which ones in true,false

