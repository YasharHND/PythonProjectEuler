from modules.numbers import divisors_sum

amicable_numbers = set()
for a in range(2, 10_000):
    if a in amicable_numbers:
        continue
    b = divisors_sum(a)
    if a == b:
        continue
    db = divisors_sum(b)
    if a == db:
        amicable_numbers.add(a)
        amicable_numbers.add(b)
answer = sum(amicable_numbers)
print(answer)
