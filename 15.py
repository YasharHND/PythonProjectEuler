history = {}


def route_count(grid, point=(0, 0)):
    global history
    if point[0] == grid and point[1] == grid:
        return 1
    relative_point = (grid - point[0], grid - point[1])
    if relative_point in history:
        return history.get(relative_point)
    count = 0
    if point[0] < grid:
        down_point = (point[0] + 1, point[1])
        to_down_count = route_count(grid, down_point)
        history.update({(grid - down_point[0], grid - down_point[1]): to_down_count})
        count += to_down_count
    if point[1] < grid:
        right_point = (point[0], point[1] + 1)
        to_right_count = route_count(grid, right_point)
        history.update({(grid - right_point[0], grid - right_point[1]): to_right_count})
        count += to_right_count
    return count


for i in range(1, 21):
    i_count = route_count(i)
    history.update({(i, i): i_count})
    print(f"{i: >2}{i_count: >14}")
