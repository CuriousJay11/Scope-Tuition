
terms=int(input("Enter num:"))
n1,n2 = 0,1
count = 0

if terms <=0:
   print("Enter the positive number:")

elif terms == 1:
   print(n1)

else:
   print("Sequence:")
   while count<terms:
      print(n1)
      nth = n1+n2
      n1 = n2
      n2 = nth
      count += 1
 
         
