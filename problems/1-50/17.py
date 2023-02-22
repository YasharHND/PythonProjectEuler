import re
from num2words import num2words

count = 0
for i in range(1, 1001):
    count += len(re.sub("[ -]", "", num2words(i)))
print(count)
