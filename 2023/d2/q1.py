from collections import defaultdict
from pprint import pprint

id_sum = 0
result = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input") as f:

    for text in f:
        verdict = True
        # loop every game

        gameset = []
        counters = defaultdict(int)

        id, sets = text.split(": ")
        sets = sets.split(";")
        id = id.split(" ")[-1]

        for set in sets:

            # loop sets

            picks = set.split(",")

            for pick in picks:
                print(pick)
                # loop every rgb

                count, colour = pick.strip().split(" ")
                counters[colour] += int(count)

                if int(count) > result[colour]:
                    verdict = False
                    break

        if verdict is True:
            id_sum += int(id)
            gameset.append(counters)
            counters = defaultdict(int)
        verdict = True
        print("game id: ", id)
        print(*gameset, sep='\n')
        print("------------------\n")

        # for count, color in enumerate(counters):

        #     if result[color] < counters[color]:
        #         verdict = False
        #     break

print(id_sum)
