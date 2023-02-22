# https://www.youtube.com/watch?v=r80peHph558
import time

powers = {
    "0": 0,
    "1": 1,
    "2": 4,
    "3": 9,
    "4": 16,
    "5": 25,
    "6": 36,
    "7": 49,
    "8": 64,
    "9": 81
}


def next_n(n):
    return sum(powers[d] for d in str(n))


ending_numbers = {
    1: False,
    89: True
}


def ends_in_89(n):
    if n in ending_numbers:
        return ending_numbers[n]
    n2 = n
    while n2 not in ending_numbers:
        n2 = next_n(n2)
    result = ending_numbers[n2]
    ending_numbers.update({n: result})
    return result


def solve():
    return len([n for n in range(1, 10000000) if ends_in_89(n)])


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to get execute...")
