import sys
from pprint import pprint


class Coords:
    def __init__(self, val,  x, y):
        self.val = val
        self.x = x
        self.y = y
        return

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Val:{self.val} x:{self.x} y:{self.y}"

    def get_adj_tl(self):
        return {"x": self.x - 1, "y": self.y - 1}

    def get_adj_tc(self):
        return {"x": self.x, "y": self.y - 1}

    def get_adj_tr(self):
        return {"x": self.x + 1, "y": self.y - 1}

    def get_adj_cl(self):
        return {"x": self.x - 1, "y": self.y}

    def get_adj_cr(self):
        return {"x": self.x + 1, "y": self.y}

    def get_adj_bl(self):
        return {"x": self.x - 1, "y": self.y + 1}

    def get_adj_bc(self):
        return {"x": self.x, "y": self.y + 1}

    def get_adj_br(self):
        return {"x": self.x + 1, "y": self.y + 1}

    def get_adj(self):
        return [
            self.get_adj_tl(),
            self.get_adj_tc(),
            self.get_adj_tr(),
            self.get_adj_cl(),
            self.get_adj_cr(),
            self.get_adj_bl(),
            self.get_adj_bc(),
            self.get_adj_br()
        ]

    def get_adj_x(self):
        return [coords["x"] for coords in self.get_adj()]

    def get_adj_y(self):
        return [coords["y"] for coords in self.get_adj()]


class Part:
    def __init__(self, partval):
        self.partval = partval
        self.coords_list = []
        return

    def insert(self, coords):
        self.coords_list.append(coords)
        return

    def length(self):
        return len(self.partval)

    def value(self):
        return int(self.partval)

    def __repr__(self):
        return f"Part: {self.partval} list: {self.coords_list}"


partsCollection = []
symbolCollection = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        line = line.rstrip("\r\n")
        parts = [part for part in line.split(".") if part.isdigit()]

        # part check
        for partstring in parts:
            part_obj = Part(partstring)
            location = line.find(partstring)

            # append every part coordinates inside part
            for idx, part in enumerate(partstring):
                part_obj.insert(Coords(part, idx + location, y))
            partsCollection.append(part_obj)

        # symbol check_call
        for x, char in enumerate(line):
            if char != ".":
                if not char.isdigit():
                    # print(f"char: {char} x:{x} y:{y}")
                    symbolCollection.append(Coords(char, x, y))
