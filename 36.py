def is_palindrome(number):
    for i in range(len(number) // 2):
        if number[i] != number[-1 - i]:
            return False
    return True


summation = 0
for i in range(1, 1_000_000):
    if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
        summation += i
print(summation)
