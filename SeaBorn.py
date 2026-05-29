#Seaborn is a library
#Used under matplotlib to plot graphs
#Used to visulaise random distributions

#Displot - Distribution Plot is a method
#Takes input as array and plots a curve corresponding to the distribution of points in array

import matplotlib.pyplot as plt
import seaborn as sns

#sns.displot([0,1,2,3,4,5])
#plt.show()

#Width of the bars is n/n-1

#sns.displot([0,1,2,3,4,5],kind='kde')
#plt.show()

#Kde - Kennel DENSITY Estimation - To show in curve format
#|-> Probability of data


#Normal Distribution
#random.normal()
from numpy import random
#loc(mean) where peak exists
#scale - flat the graph distributed
#size =  shape of returned array

#Generate a random normal distribution of size 2x3
#Continuos Data
#x = random.normal(size=(2,3))
#print(x)

#x = random.normal(loc=1,scale=2,size=(2,3))
#print(x)

#sns.displot(random.normal(size=100),kind='kde')
#plt.show()

#Given 10 trials for coin to toss to  give 10 data points
#Bionomial Distribution
#Discrete Data
#x = random.binomial(n=10,p=0.5,size=10)
#print(x)

#sns.displot(random.binomial(n=10,p=0.5,size=1000))
#plt.show()

#Location = Where the output will be near

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#data = {"normal":random.normal(loc=50,scale=5,size=1000),
#        "Binomial" : random.binomial(n=50,p=0.5,size=1000) 
#        }
#sns.displot(data,kind='kde')
#plt.show()

#Poission Distribution
#Size = Shape of returned array
#Lam = Rate/average no of occurances

#from numpy import random
#x = random.poisson(lam=2,size=10)
#print(x)

#3from numpy import random
#data = random.poisson(lam=5,size=1000)
#sns.histplot(data)
#plt.show()

#Uniform Distribution - Equal chance of coming
#Low- Min
#High - Max
#Size - Values
# Syntax - random.uniform(low,high,size)

from numpy import random
#x = random.uniform(low=1,high=10,size=5)
#print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#x = random.uniform(low=1,high=10,size=5)
#sns.histplot(x)
#plt.show()

#Exponential Distribution

x=random.exponential(scale=2,size=10)#Scale- average waiting time
sns.histplot(x)
plt.show()

