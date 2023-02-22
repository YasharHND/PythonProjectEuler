def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        summation = sum_of_digits(a ** b)
        max_sum = max(max_sum, summation)
print(max_sum)
