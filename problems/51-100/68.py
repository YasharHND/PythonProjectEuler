from itertools import permutations


class Line:
    def __init__(self):
        self.numbers = [0 for _ in range(3)]

    def add(self, number, index):
        self.numbers[index] = number


class Gon:
    def __init__(self, side_count):
        self.lines = [Line() for _ in range(side_count)]
        self.pointer = 0

    def add(self, number):
        node_idx = next(idx for idx, value in enumerate(self.lines[self.pointer].numbers) if value == 0)
        self.lines[self.pointer].add(number, node_idx)
        if self.pointer < len(self.lines) - 1 and node_idx > 0:
            if self.pointer == 0 and node_idx == 1:
                self.lines[-1].add(number, 2)
            else:
                self.lines[self.pointer + 1].add(number, 1 if node_idx == 2 else 1)
        if node_idx == 2:
            self.pointer += 1

    def add_all(self, numbers):
        for number in numbers:
            self.add(number)

    def is_magical(self):
        target = sum(self.lines[0].numbers)
        return all(sum(line.numbers) == target for line in self.lines[1:])

    def get_value(self):
        min_value = (len(self.lines) * 2) + 1
        start_idx = 0
        for idx, line in enumerate(self.lines):
            if line.numbers[0] < min_value:
                min_value = line.numbers[0]
                start_idx = idx
        self.lines = self.lines[start_idx:] + self.lines[:start_idx]
        return "".join(str(n) for line in self.lines for n in line.numbers)


maximum = 0
for group in permutations(range(1, 11)):
    gon = Gon(5)
    gon.add_all(group)
    if gon.is_magical():
        gon_value = gon.get_value()
        if len(gon_value) == 16:
            print(gon_value)
            maximum = max(maximum, int(gon_value))
print(f"Answer: {maximum}")
