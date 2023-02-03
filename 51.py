from itertools import product
import math


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def cases(digits, stars):
    out = []
    for i in range(digits - (stars - 1)):
        left = [1 for _ in range(i)] + [0]
        if stars > 1:
            for right in cases(digits - len(left), stars - 1):
                out.append(left + right)
        else:
            out.append(left + [1 for _ in range(digits - len(left))])
    return out


def fill(template, fixed, repeating):
    out = ""
    fixed_idx = 0
    for i in range(len(template)):
        if template[i]:
            out += str(fixed[fixed_idx])
            fixed_idx += 1
        else:
            out += str(repeating)
    return int(out)


answer = None
digit_length = 3
while True:
    for repeating_length in range(2, digit_length):
        for pattern in cases(digit_length, repeating_length):
            for other_digits in product(range(10), repeat=digit_length - 2):
                if other_digits[0] == 0:
                    continue
                family = []
                for repeating_digit in range(10):
                    if pattern[0] == 0 and repeating_digit == 0:
                        continue
                    generated = fill(pattern, other_digits, repeating_digit)
                    if is_prime(generated):
                        family.append(generated)
                if len(family) == 8:
                    answer = family[0]
                    print(answer)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        digit_length += 1
        continue
    break
