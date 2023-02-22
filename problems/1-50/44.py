import math


def pentagon(n):
    return (n * ((3 * n) - 1)) // 2


# https://stackoverflow.com/a/37390529/19581178
def is_pentagonal(n):
    k = (math.sqrt(24 * n + 1) + 1) / 6
    return k.is_integer()


pentagons = []
i = 1
while True:
    new_pentagon = pentagon(i)
    for previous_pentagon in pentagons:
        sub = new_pentagon - previous_pentagon
        if is_pentagonal(sub):
            add = new_pentagon + previous_pentagon
            if is_pentagonal(add):
                print(sub)
                break
    else:
        pentagons.append(new_pentagon)
        i += 1
        continue
    break
