import math
import cmath
a= 1
b=5
c=6

d=(b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(sol1,sol2)

print(math.sqrt(16))

number = 16
sqrt = number ** 0.5
print(sqrt) 

year = int(input("What year?: "))

if(year%400==0) and (year%100 == 0):
 print("Leap year: ",year)
elif (year%4 == 0) and (year% 100!=0):
 print("not a leap year",year)
else:
 print(year, "Not a leap year")
