from argparse import ArgumentParser
from math import prod
from pathlib import Path


def is_lower(data, x, y):

    p = data[x][y]

    if x + 1 < len(data) and p >= data[x+1][y]:
        return False

    if y + 1 < len(data[x]) and p >= data[x][y+1]:
        return False

    if x > 0 and p >= data[x-1][y]:
        return False

    if y > 0 and p >= data[x][y-1]:
        return False

    return True


def calc_risk_level(points):
    return sum(points)+len(points)


def calc_basin_size(x, y, data):

    visited = set()

    def visit(x, y):

        visited.add((x, y))

        if x < 0 or y < 0 or x >= len(data) or y >= len(data[x]) or data[x][y] == 9:
            return 0

        return 1 + sum([visit(*p) for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if p not in visited])

    return visit(x, y)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")
    data = [[int(x) for x in list(row)] for row in lines]

    results = []
    results_loc = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_lower(data, i, j):
                results_loc.append((i, j))
                results.append(data[i][j])

    print(calc_risk_level(results))

    basin_sizes = [calc_basin_size(x, y, data) for x, y in results_loc]
    print(prod(sorted(basin_sizes)[-3:]))
