import sys

partCollection = []

with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        candidates = line.split(".")
        candidates = [candidate.strip()
                      for candidate in candidates if candidate.strip()]
        print(candidates)
