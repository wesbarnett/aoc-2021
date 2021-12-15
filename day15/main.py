from argparse import ArgumentParser
from pathlib import Path


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    data = [[int(x) for x in row] for row in Path(args.infile).read_text().rstrip("\n").split("\n")]
    nrows = len(data)
    ncols = len(data[0])

    risk = [[0 for x in row] for row in data]

    risk[0][0] = 0

    for col in range(1, ncols):
        risk[0][col] = data[0][col] + risk[0][col-1]

    for row in range(1, nrows):
        risk[row][0] = data[row][0] + risk[row-1][0]

    for row in range(1, nrows):
        for col in range(1, ncols):
            risk[row][col] += data[row][col] + min(risk[row-1][col], risk[row][col-1])

    print(risk[-1][-1])
