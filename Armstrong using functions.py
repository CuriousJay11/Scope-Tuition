def is_armstrong(num):

    num_str = str(num)
    n = len(num_str)
    
    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    
    
    return sum_of_powers == num


number = 153
if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")


   

