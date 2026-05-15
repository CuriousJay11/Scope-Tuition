#Return a value from the function - Return statement

def find_square(num):
    result = num*num
    return result
#Any code after return will not be executed

square = find_square(3)
print('square:',square)