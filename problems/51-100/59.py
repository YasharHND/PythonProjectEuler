import string
from itertools import product

with open("59.txt", "r") as file:
    decrypted_message = list(map(int, file.readline().split(",")))

common_words = ["and", "the", "is"]


def has_common_words(message):
    for word in common_words:
        if " " + word not in message or word + " " not in message:
            return False
    return True


for combination in product(string.ascii_lowercase, repeat=3):
    key = list(map(ord, combination))
    encrypted_message = ""
    max_i = 0
    for i, digit in enumerate(decrypted_message):
        max_i = max(max_i, i)
        char = chr(digit ^ key[i % 3])
        encrypted_message += char
    if has_common_words(encrypted_message):
        print(encrypted_message)
        print(sum(ord(c) for c in encrypted_message))
        break
