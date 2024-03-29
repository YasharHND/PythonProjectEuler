import string

from modules.numbers import is_perfect_square


def word_value(word):
    return sum([string.ascii_uppercase.index(c) + 1 for c in word])


# https://www.youtube.com/watch?v=fzhYE2v3ojY
def is_triangle(number):
    testing_number = 1 + (8 * number)
    return is_perfect_square(testing_number)


with open("42.txt", "r") as file:
    words = file.readline().strip()[1: -1].split('","')
answer = sum(is_triangle(word_value(word)) for word in words)
print(answer)
