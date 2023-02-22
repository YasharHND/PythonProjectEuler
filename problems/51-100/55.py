from modules.strings import is_palindrome


def reverse(number):
    return int(str(number)[::-1])


def is_lychrel(nuber):
    summation = nuber
    for _ in range(49):
        summation += reverse(summation)
        if is_palindrome(str(summation)):
            return False
    return True


count = 0
for n in range(1, 10000):
    if is_lychrel(n):
        count += 1
print(count)
