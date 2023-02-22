def sequence_length(n):
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        length += 1
    return length


target_number = 0
max_sequence_length = 0
for number in range(1000000):
    number_sequence_length = sequence_length(number)
    if number_sequence_length > max_sequence_length:
        max_sequence_length = number_sequence_length
        target_number = number
print(target_number)
