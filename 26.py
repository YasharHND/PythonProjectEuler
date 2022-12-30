def recurring_cycles_count(numerator, denominator):
    reminders = []
    decimals = []
    quotient, reminder = divmod(numerator, denominator)
    while reminder not in reminders:
        reminders.append(reminder)
        quotient, reminder = divmod(reminder * 10, denominator)
        decimals.append(quotient)
    return len(decimals) - decimals.index(quotient)


longest_count = 0
longest_digit = 0
for d in range(1, 1000):
    count = recurring_cycles_count(1, d)
    if count > longest_count:
        longest_count = count
        longest_digit = d
print(longest_digit)
