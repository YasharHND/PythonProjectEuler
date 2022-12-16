n1 = 1
n2 = 2
out = 0
while n2 < 4000000:
    if n2 % 2 == 0:
        out += n2
    n1, n2 = n2, n1 + n2
print(out)
