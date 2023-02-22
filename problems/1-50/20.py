from modules.numbers import factorial

answer = sum(map(int, [c for c in str(factorial(100))]))
print(answer)
