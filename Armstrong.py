num1 = int(input("Enter a 3 digit number: "))

sum = 0
temp = num1

while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//= 10 

if num1==sum:
   print("It is a armstrong number")
else:
    print("No it is not an armstrong number")

