#Double all numbers using map function, Temperature Chnaging map, Find Cube of number using map()
#Create lambda for checking postive or negative,  Find maximum number using *args, Employee database using **kwargs, Restaurant Order system using both(args and kwargse)

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)

numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda x: x ** 3, numbers))

print(cubes)

check = lambda x: "Positive" if x >= 0 else "Negative"

print(check(10))
print(check(-5))

def find_max(*args):
    print("Maximum number is:", max(args))

find_max(10, 50, 25, 80, 40)

def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(
    name="Rahul",
    age=25,
    department="IT",
    salary=50000
)