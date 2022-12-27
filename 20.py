def factorial(n):
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


answer = sum(map(int, [c for c in str(factorial(100))]))
print(answer)
