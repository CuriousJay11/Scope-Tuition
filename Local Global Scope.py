#Scope

# A variable is only available from 
# inside the region it is created this is called scope

#Local Scope
# Variable created inside function belongs to the local scope 
# and can be used only inside the function

def myfn():
    x=300
    print(x)
myfn()
#print x

#It will show error when u add print x at the end because you
# cannot call it outside the function

def myfn():
    x=100
    def innerfn():
        print(x)
    innerfn()

myfn()

#Function inside a function

#Global Scope
#|-> Variable created in the main body of code in gloabl and
# belongs to the global scope

x = 300 #global
def nf():
    print(x)
nf()
print(x)

x=20
def fn():
    x=30
    print(x)
fn()
print(x)

x=500
def my():
    global x #Global keyword
    x = 400
my()
print (x)


