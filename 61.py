from itertools import permutations

p3 = [(n * (n + 1)) // 2 for n in range(45, 141)]
p4 = [n ** 2 for n in range(32, 100)]
p5 = [(n * ((3 * n) - 1)) // 2 for n in range(26, 82)]
p6 = [n * ((2 * n) - 1) for n in range(23, 71)]
p7 = [(n * ((5 * n) - 3)) // 2 for n in range(21, 64)]
p8 = [n * ((3 * n) - 2) for n in range(19, 59)]
after_p3 = [p4, p5, p6, p7, p8]


for permutation in permutations(range(5)):
    for k1 in p3:
        k1rd = str(k1)[-2:]
        for k2 in list(filter(lambda x: str(x)[:2] == k1rd, after_p3[permutation[0]])):
            k2rd = str(k2)[-2:]
            for k3 in list(filter(lambda x: str(x)[:2] == k2rd, after_p3[permutation[1]])):
                k3rd = str(k3)[-2:]
                for k4 in list(filter(lambda x: str(x)[:2] == k3rd, after_p3[permutation[2]])):
                    k4rd = str(k4)[-2:]
                    for k5 in list(filter(lambda x: str(x)[:2] == k4rd, after_p3[permutation[3]])):
                        k5rd = str(k5)[-2:]
                        for k6 in list(filter(lambda x: str(x)[:2] == k5rd and str(x)[-2:] == str(k1)[:2], after_p3[permutation[4]])):
                            result = [k1, k2, k3, k4, k5, k6]
                            print(result)
                            print(sum(result))
