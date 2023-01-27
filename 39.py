def possibilities_count(perimeter):
    count = 0
    for c in range((perimeter // 3) + 1, perimeter - 1):
        remaining = perimeter - c
        for a in range(1, remaining // 2):
            b = remaining - a
            if (a ** 2) + (b ** 2) == c ** 2:
                count += 1
    return count


max_perimeter = 0
max_possibilities = 0
for p in range(3, 1001):
    p_count = possibilities_count(p)
    if p_count > max_possibilities:
        max_perimeter = p
        max_possibilities = p_count
print(max_perimeter)
