import math
import time


# https://www.youtube.com/watch?v=mo5J_EFtZMA
def solve(limit):
    line_lengths = {}
    for m in range(2, math.ceil(math.sqrt(limit / 2)) + 1):
        m_square = m ** 2
        for n in range(1, m):
            if (m + n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            n_square = n ** 2
            a, b, c = m_square - n_square, 2 * m * n, m_square + n_square
            k = 1
            while True:
                length = k * (a + b + c)
                if length > limit:
                    break
                count = line_lengths[length] + 1 if length in line_lengths else 1
                line_lengths[length] = count
                k += 1
    return sum(1 for x in line_lengths.values() if x == 1)


srt = time.time()
answer = solve(1_500_000)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
