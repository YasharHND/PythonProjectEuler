# https://www.youtube.com/watch?v=WVsreMLbcNg
cubes = {}
i = 22
while True:
    cube = i ** 3
    digits = "".join(sorted(str(cube)))
    if digits in cubes:
        previous_value = cubes.get(digits)
        previous_count = previous_value.get("count")
        if previous_count == 4:
            print(previous_value.get("smallest"))
            break
        previous_value.update({"count": previous_count + 1})
    else:
        cubes.update({
            digits: {
                "count": 1,
                "smallest": cube
            }
        })
    i += 1
