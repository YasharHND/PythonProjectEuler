# https://www.educative.io/answers/project-euler-63-powerful-digit-counts
import math

result = 0
least = 1
largest = 9
n = 1
while least < 10:
    least = math.ceil((10 ** (n - 1)) ** (1 / n))
    result += (largest - least) + 1
    n += 1
print(result)
