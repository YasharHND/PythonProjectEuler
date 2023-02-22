coins = [
    200,
    100,
    50,
    20,
    10,
    5,
    2,
    1
]


def combinations(idx, target):
    out = []
    for i, current_coin in enumerate(coins[idx:]):
        k = i + idx
        remaining = target - current_coin
        if remaining > 0:
            inner_idx = k if remaining >= current_coin else k + 1
            for inner_combination in combinations(inner_idx, remaining):
                out.append([current_coin] + inner_combination)
        else:
            out.append([current_coin])
    return out


answer = len(combinations(0, 200))
print(answer)
