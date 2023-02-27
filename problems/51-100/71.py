import time


# https://www.youtube.com/watch?v=qRCKO6Az4QY
def solve(limit):
    return 2 + 3 * (limit // 7 - 1)


srt = time.time()
answer = solve(10 ** 6)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
