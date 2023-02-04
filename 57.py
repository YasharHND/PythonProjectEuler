def digits_count(number):
    return len(str(number))


count = 0
np2 = 1
np1 = 1
dp2 = 0
dp1 = 1
for _ in range(1000):
    npn = np1 * 2 + np2
    np2, np1 = np1, npn
    dpn = dp1 * 2 + dp2
    dp2, dp1 = dp1, dpn
    if digits_count(npn) > digits_count(dpn):
        count += 1
print(count)
