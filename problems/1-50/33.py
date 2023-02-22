import functools
from fractions import *

fractions = []
for nl in range(1, 10):
    for nr in range(nl, 10):
        numerator = int(f"{nl}{nr}")
        dl = nr
        for dr in range(1 if nr > nl else nr + 1, 10):
            denominator = int(f"{dl}{dr}")
            if numerator / denominator == nl / dr:
                fraction = Fraction(numerator=numerator, denominator=denominator)
                fractions.append(fraction)

product = functools.reduce(lambda x, y: x * y, fractions)
answer = product.denominator
print(answer)
