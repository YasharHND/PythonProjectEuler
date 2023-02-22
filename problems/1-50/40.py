from functools import reduce

dns = []
dn = 1
last_idx = 0
n = 1
while dn <= 1_000_000:
    fraction = str(n)
    idx = dn - 1
    new_last_idx = last_idx + len(fraction)
    if idx < new_last_idx:
        dns.append(int(fraction[idx - last_idx]))
        dn *= 10
    last_idx = new_last_idx
    n += 1
answer = reduce(lambda x, y: x * y, dns)
print(answer)
