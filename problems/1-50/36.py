from modules.strings import is_palindrome

summation = 0
for i in range(1, 1_000_000):
    if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
        summation += i
print(summation)
