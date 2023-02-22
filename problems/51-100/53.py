from modules.numbers import factorial


def combinatoric_selection(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


count = 0
for i in range(1, 101):
    for j in range(1, i + 1):
        if combinatoric_selection(i, j) > 1_000_000:
            count += 1
print(count)
