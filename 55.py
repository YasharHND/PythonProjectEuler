def is_palindrome(number):
    str_number = str(number)
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-1 - i]:
            return False
    return True


def reverse(number):
    return int(str(number)[::-1])


def is_lychrel(nuber):
    summation = nuber
    for _ in range(49):
        summation += reverse(summation)
        if is_palindrome(summation):
            return False
    return True


count = 0
for n in range(1, 10000):
    if is_lychrel(n):
        count += 1
print(count)
