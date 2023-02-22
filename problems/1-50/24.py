import itertools

for i, item in enumerate(itertools.permutations(range(10)), start=1):
    if i == 1_000_000:
        print("".join(map(str, item)))
        break
