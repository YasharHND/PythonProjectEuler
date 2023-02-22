def is_palindrome(number):
    for i in range(len(number) // 2):
        if number[i] != number[-1 - i]:
            return False
    return True
