i = 2
n1 = 1
n2 = 1
while True:
    i += 1
    n1, n2 = n2, n1 + n2
    if len(str(n2)) == 1000:
        print(i)
        break
