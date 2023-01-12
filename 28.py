directions = {
    "R": {
        "moveX": lambda x: x + 1,
        "moveY": lambda y: y,
        "nextDirection": "D"
    },
    "D": {
        "moveX": lambda x: x,
        "moveY": lambda y: y - 1,
        "nextDirection": "L"
    },
    "L": {
        "moveX": lambda x: x - 1,
        "moveY": lambda y: y,
        "nextDirection": "U"
    },
    "U": {
        "moveX": lambda x: x,
        "moveY": lambda y: y + 1,
        "nextDirection": "R"
    }
}


def spiral(n):
    summation, x, y = 0, 0, 0
    direction = directions.get("R")
    new_circle = False
    for i in range(1, n ** 2 + 1):
        if new_circle:
            direction = directions.get("D")
            new_circle = False
        if abs(x) == abs(y):
            summation += i
            if x >= 0 and y >= 0:
                new_circle = True
            else:
                direction = directions.get(direction.get("nextDirection"))
        x = direction.get("moveX")(x)
        y = direction.get("moveY")(y)
    return summation


answer = spiral(1001)
print(answer)
