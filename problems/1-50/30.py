def sum_of_digits(number, power):
    return sum(int(digit) ** power for digit in str(number))


answer = 0
for n in range(2, 1000000):
    d_sum = sum_of_digits(n, 5)
    if d_sum == n:
        answer += n
print(answer)
