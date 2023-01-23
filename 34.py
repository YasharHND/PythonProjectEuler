from functools import reduce


factorials = [1]
for i in range(1, 10):
    factorials.append(reduce(lambda x, y: x * y, [i for i in range(1, i + 1)]))


def digits_factorial(number):
    return sum(factorials[int(digit)] for digit in str(number))


summation = 0
for i in range(145, factorials[9]):
    if digits_factorial(i) == i:
        summation += i
print(summation)
