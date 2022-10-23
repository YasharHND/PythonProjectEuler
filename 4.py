def is_palindromic(number):
    str_num = str(number)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-1 - i]:
            return False
    return True


palindromic_numbers = []
for x in reversed(range(100, 1000)):
    for y in reversed(range(100, 1000)):
        product = x * y
        if is_palindromic(product):
            palindromic_numbers.append(product)
print(max(palindromic_numbers))
