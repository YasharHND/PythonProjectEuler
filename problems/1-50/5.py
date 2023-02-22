def is_evenly_divisible(number):
    for i in range(2, 21):
        if number % i != 0:
            return False
    return True


i = 20
while True:
    i += 20
    if is_evenly_divisible(i):
        print(i)
        break
