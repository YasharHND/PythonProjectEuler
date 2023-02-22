import string

with open("22.txt", "r") as file:
    names = file.readline().strip()[1:-1].split('","')

answer = 0
names.sort()
for i, name in enumerate(names):
    answer += (i + 1) * sum([string.ascii_uppercase.index(c) + 1 for c in name])
print(answer)
