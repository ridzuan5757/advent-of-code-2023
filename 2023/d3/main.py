import sys


def check_adjacent(f, coords):
    candidates = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    for candidate in candidates:
        y, x = tuple(map(lambda x, y: x + y, coords, candidate))

        try:
            print("number grid check",
                  f[coords[0]][coords[1]], coords, "adjacent value: ", f[y][x])
        except Exception:
            pass

        try:
            if not f[y][x].isnumeric() and f[y][x] != ".":
                return True
        except Exception:
            pass
    return False


sum = []
is_real_part = False

with open(sys.argv[1]) as f:

    lines = f.readlines()
    grid_data = [line.strip().split()[0] for line in lines]

    for y, line in enumerate(grid_data):

        line_length = len(line)
        part_number = ""

        for x, char in enumerate(line):

            if char.isnumeric():
                print("char ", char)

                part_number += char
                is_adjacent = check_adjacent(grid_data, (y, x))

                # print(char, "adjacent: ", is_adjacent, "\n")
                is_real_part |= is_adjacent

                try:
                    if grid_data[y][x+1].isnumeric() is False:

                        print("next item is not a number", grid_data[y][x+1])

                        if is_real_part and part_number != "":
                            print(part_number, "has adjacent symbol\n\n")
                            sum.append(int(part_number))
                            is_real_part = False

                        part_number = ""
                except Exception:
                    pass

print(sum)
val = 0
for x in sum:
    val += x

print(val)
