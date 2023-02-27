import sympy

target = []
k = 1
while True:
    if len(sympy.primefactors(k)) == 4:
        target.append(k)
        if len(target) == 4:
            print(target[0])
            break
    else:
        target.clear()
    k += 1
