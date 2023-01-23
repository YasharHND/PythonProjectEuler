expected = [str(n) for n in range(1, 10)]


def is_pandigital(number):
    return sorted(number) == expected


max_pandigital = 0
for i in range(1, 10000):
    concatenated = ""
    n = 1
    while True:
        concatenated += str(i * n)
        if len(concatenated) > 9:
            break
        if len(concatenated) == 9 and is_pandigital(concatenated):
            max_pandigital = max(max_pandigital, int(concatenated))
        n += 1
print(max_pandigital)
