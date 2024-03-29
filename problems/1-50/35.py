from modules.primes import is_prime


def get_rotations(number):
    out = []
    str_number = str(number)
    for i in range(len(str_number)):
        left = str_number[i:]
        right = str_number[:i]
        out.append(int("".join(left + right)))
    return out


circular_primes = {2}
for i in range(3, 1_000_000):
    if i in circular_primes or not is_prime(i):
        continue
    rotations = get_rotations(i)
    if all(is_prime(rotation) for rotation in rotations):
        circular_primes.update(rotations)
answer = len(circular_primes)
print(answer)
