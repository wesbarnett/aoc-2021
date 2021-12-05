from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def horizontal_line(x1, y1, x2, y2, counter):
    if y1 > y2:
        y2, y1 = y1, y2
    for i in range(y1, y2+1):
        counter[(x1, i)] += 1

    return counter


def vertical_line(x1, y1, x2, y2, counter):
    if x1 > x2:
        x2, x1 = x1, x2
    for i in range(x1, x2+1):
        counter[(i, y1)] += 1

    return counter


def diagonal_line(x1, y1, x2, y2, counter):

    if x1 > x2:
        x_dir = -1
        x2 -= 1
    else:
        x_dir = 1
        x2 += 1

    if y1 > y2:
        y_dir = -1
        y2 -= 1
    else:
        y_dir = 1
        y2 += 1

    for i, j in zip(range(x1, x2, x_dir), range(y1, y2, y_dir)):
        counter[(i, j)] += 1

    return counter


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    counter = Counter()
    for line in lines:
        item = line.split(" -> ")
        x1, y1 = tuple([int(x) for x in item[0].split(",")])
        x2, y2 = tuple([int(x) for x in item[1].split(",")])

        # Only consider horizontal or vertical lines
        if x1 == x2:
            counter = horizontal_line(x1, y1, x2, y2, counter)
        elif y1 == y2:
            counter = vertical_line(x1, y1, x2, y2, counter)

    result = sum(v >= 2 for k, v in counter.items())

    print(result)

    counter = Counter()
    for line in lines:
        item = line.split(" -> ")
        x1, y1 = tuple([int(x) for x in item[0].split(",")])
        x2, y2 = tuple([int(x) for x in item[1].split(",")])

        if x1 == x2:
            counter = horizontal_line(x1, y1, x2, y2, counter)
        elif y1 == y2:
            counter = vertical_line(x1, y1, x2, y2, counter)
        else:
            counter = diagonal_line(x1, y1, x2, y2, counter)

    result = sum(v >= 2 for k, v in counter.items())

    print(result)