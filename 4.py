def is_palindrome(number):
    str_number = str(number)
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-1 - i]:
            return False
    return True


largest_palindrome = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        product = x * y
        if is_palindrome(product):
            if product > largest_palindrome:
                largest_palindrome = product

print(largest_palindrome)
