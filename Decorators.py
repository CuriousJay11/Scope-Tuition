#Decorators
# Lets you add extra behaviour to a fn without changing the functions code
#It is a function that takes another fn as input & return as a new fn
#  @decorator_name
# A basic decorator that uppercases the return value of the decorated fn

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def func():
    return 'Hello Mcqueen'
print(func())

#OUTPUT = HELLO MCQUEEN


print("Hello\nMcqueen")

#Multiple Decorators

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def func():
    return 'Hello Mcqueen'
    return 'Hello'   #One function = One return
@changecase 
def otherfn():
    return 'I am speed'
print(func())
print(otherfn())

#Function with arguements can also be decorated

def cc(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@cc
def myfn (name):
    return "Hello  " + name
print (myfn("Jackson Storm"))

# How to check if num is even or not using decorators
num = int(input("Enter a number: "))

def check_even(func):
    def mynum():
        n = func()
        if n % 2 == 0:
            print(n,"is Even")
        else:
            print(n,"is Odd")
        return n
    return mynum

@check_even
def get_number():
    return num

get_number()

#Structure

#def decorator(func):
   # def inner():
 #       {code}
 #   func()
  #  return inner

        

