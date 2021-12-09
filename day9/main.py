from argparse import ArgumentParser
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


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")
    data = [[int(x) for x in list(row)] for row in lines]

    results = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_lower(data, i, j):
                results.append(data[i][j])

    print(calc_risk_level(results))
