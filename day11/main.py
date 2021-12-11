from argparse import ArgumentParser
from pathlib import Path


def flash_sequence(i, j, data, flashed):

    def flash(i, j):
        if data[i][j] > 9 and (i, j) not in flashed:
            flashed.add((i, j))
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x, y) != (i, j) and x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
                        data[x][y] += 1
                        flash(x, y)

    flash(i, j)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    data = [[int(x) for x in row] for row in lines]

    flashes = 0
    step = 0
    while True:
        flashed = set()

        data = [[x + 1 for x in row] for row in data]

        for i, row in enumerate(data):
            for j, x in enumerate(row):
                flash_sequence(i, j, data, flashed)

        # Part 2 - first step all fish flash at same time
        if len(list(flashed)) == len(data[0])*len(data):
            all_flash_step = step+1
            break

        for x, y in list(flashed):
            data[x][y] = 0
            # Part 1 - how many flashes after 100 steps
            if step < 100:
                flashes += 1

        step += 1

    print(flashes)
    print(all_flash_step)
