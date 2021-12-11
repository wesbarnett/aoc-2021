from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def is_valid_point(x, y, data):
    return x >= 0 and x < len(data) and y >= 0 and y < len(data[x])


def neighbors(i, j, data):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (x, y) != (i, j) and is_valid_point(x, y, data):
                yield x, y


def do_flashing(i, j, data, flashed):

    def flash(i, j):
        if data[i][j] > 9 and (i, j) not in flashed:
            flashed.add((i, j))
            for x, y in neighbors(i, j, data):
                data[x][y] += 1
                flash(x, y)

    flash(i, j)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    data = [[int(x) for x in row] for row in lines]
    size = len(data)*len(data[0])

    flashes = Counter()
    step = 1
    flashed = set()

    while len(list(flashed)) != size:

        data = [[x + 1 for x in row] for row in data]

        flashed = set()
        for i, row in enumerate(data):
            for j, _ in enumerate(row):
                do_flashing(i, j, data, flashed)

        flashes[step] += flashes[step-1]
        for x, y in list(flashed):
            data[x][y] = 0
            flashes[step] += 1

        step += 1

    print(f"Part 1 result: {flashes[100]}")
    print(f"Part 2 result: {step-1}")
