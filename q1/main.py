result = 0

with open("input") as f:
    for line in f:
        candidates = []
        for i in line:
            if i.isdigit():
                candidates.append(i)

        if len(candidates) < 2:
            val = candidates[0] + candidates[0]
        else:
            val = candidates[0] + candidates[-1]

        print(candidates)
        print(val)
        result += int(val)

print(result)
