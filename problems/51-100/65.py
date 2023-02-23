import time

from fractions import Fraction


# https://www.youtube.com/watch?v=iQ1KT8W-Y6U
# works for limits bigger than 2
def coefficients_of_e(limit):
    out = [1, 2]
    variable_coefficient = 2
    for i in range(1, limit - 2):
        if i % 3 == 0:
            variable_coefficient += 2
            out.append(variable_coefficient)
        else:
            out.append(1)
    return out


def convergent_of_e(at):
    fraction = 0
    for coefficient in reversed(coefficients_of_e(at)):
        fraction = Fraction(1, coefficient + fraction)
    return 2 + fraction


def solve():
    convergent = convergent_of_e(100)
    return sum(int(d) for d in str(convergent.numerator))


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
