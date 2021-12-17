from argparse import ArgumentParser
from pathlib import Path


class TargetArea:

    def __init__(self, x1, x2, y1, y2):
        if x1 < x2:
            self.x1 = x1
            self.x2 = x2
        else:
            self.x1 = x2
            self.x2 = x1

        if y1 < y2:
            self.y1 = y1
            self.y2 = y2
        else:
            self.y1 = y2
            self.y2 = y1

    def __call__(self, x, y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return "success"
        else:
            return "keep going"


class Probe:

    def __init__(self, vx, vy, ta):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.ta = ta
        self.maxy = 0

    def __call__(self):
        self.x += self.vx
        self.y += self.vy
        print(self.x, self.y)

        if self.y > self.maxy:
            self.maxy = self.y

        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1

        self.vy -= 1

        return self.ta(self.x, self.y)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    ta = TargetArea(20, 30, 10, -5)
    ta = TargetArea(211, 232, -124, -69)

    probe = Probe(21, 123, ta)
    status = probe()
    while status == "keep going":
        status = probe()

    print(status)
    print(probe.x, probe.y)
    print(probe.maxy)
