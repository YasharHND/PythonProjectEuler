def as_list(number):
    return sorted(list(str(number)))


def contain_same_digits(number_list, other):
    return number_list == as_list(other)


x = 1
while True:
    x_list = as_list(x)
    for m in range(2, 7):
        if not contain_same_digits(x_list, m * x):
            break
    else:
        print(x)
        break
    x += 1
