#When a function calls itself

def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

def factorial(n):
    if n==0 or n==1:
        return 1
    #Recursive Case
    else:
        return n* factorial(n-1)
    
print(factorial(5))
