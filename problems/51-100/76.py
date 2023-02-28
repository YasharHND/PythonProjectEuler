import time


# https://www.youtube.com/watch?app=desktop&v=040CtMTGx_Q
def combinations_count(number):
    matrix = [[0 if col else 1 for col in range(number + 1)] for _ in range(number)]
    for row in range(1, number):
        for col in range(1, number + 1):
            value = matrix[row - 1][col]
            if col >= row:
                value += matrix[row][col - row]
            matrix[row][col] = value
    return matrix[number - 1][number]


def solve():
    return combinations_count(100)


srt = time.time()
answer = solve()
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
