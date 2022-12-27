def sum_of_divisors(n):
    return 1 + sum([k for k in range(2, (n // 2) + 1) if n % k == 0])


amicable_numbers = set()
for a in range(2, 10_000):
    if a in amicable_numbers:
        continue
    b = sum_of_divisors(a)
    if a == b:
        continue
    db = sum_of_divisors(b)
    if a == db:
        amicable_numbers.add(a)
        amicable_numbers.add(b)
answer = sum(amicable_numbers)
print(answer)
