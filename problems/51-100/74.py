import time

from modules.numbers import factorial

factorials = [1] + [factorial(i) for i in range(1, 10)]


def digits_factorial(number):
    return sum(factorials[int(digit)] for digit in str(number))


def chain_length(number):
    chain = [number]
    while True:
        number = digits_factorial(number)
        if number in chain:
            return len(chain)
        chain.append(number)


def solve(limit):
    count = 0
    for i in range(1, limit + 1):
        if chain_length(i) == 60:
            count += 1
    return count


srt = time.time()
answer = solve(10 ** 6)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
