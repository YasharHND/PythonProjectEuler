triangle = []
with open("67.txt") as file:
    for line in file:
        triangle.append(list(map(int, line.strip().split())))

while len(triangle) > 1:
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i+1])
    triangle.pop()

print(triangle[0][0])
