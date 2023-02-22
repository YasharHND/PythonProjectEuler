from modules.strings import is_palindrome

largest_palindrome = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        product = x * y
        if is_palindrome(str(product)):
            if product > largest_palindrome:
                largest_palindrome = product

print(largest_palindrome)
