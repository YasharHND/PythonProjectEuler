from modules.numbers import factorial

factorials = [1] + [factorial(i) for i in range(1, 10)]


def digits_factorial(number):
    return sum(factorials[int(digit)] for digit in str(number))


summation = 0
for i in range(145, factorials[9]):
    if digits_factorial(i) == i:
        summation += i
print(summation)
