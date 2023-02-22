sum_square = sum([n ** 2 for n in range(1, 101)])
square_sum = sum([n for n in range(1, 101)]) ** 2
print(square_sum - sum_square)
