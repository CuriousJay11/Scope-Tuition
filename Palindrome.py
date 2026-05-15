num = int(input("Enter a number: "))

def palindrome(n):
    return str(n) == str(n)[::-1]

if palindrome(num):
    print(num, "is a palindrome!")
else:
    print(num, "is not a palindrome.")



word = str(input("Enter a word: "))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if is_palindrome(word):
    print(word, "is a palindrome!")
else:
    print(word, "is not a palindrome.")
