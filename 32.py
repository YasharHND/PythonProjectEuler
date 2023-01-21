import itertools


def to_integer(collection):
    return int(''.join(collection))


summation = set()
sum2 = 0
for permutation in itertools.permutations("123456789", 9):
    for left in range(1, 9):
        for right in range(left + 1, 9):
            m1 = to_integer(permutation[:left])
            m2 = to_integer(permutation[left:right])
            product = to_integer(permutation[right:])
            if m1 * m2 == product:
                summation.add(product)
                sum2 += product
answer = sum(summation)
print(answer)
