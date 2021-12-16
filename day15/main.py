from argparse import ArgumentParser
import heapq
from pathlib import Path


def tile_data(data, n):

    nrows_orig = len(data)
    ncols_orig = len(data[0])

    ncols = len(data[0])*n
    nrows = len(data)*n

    data_tmp = [[[0 for _ in range(ncols_orig)] for _ in range(nrows_orig)] for _ in range(n*2)]
    data_tiled = [[0 for _ in range(ncols)] for _ in range(nrows)]

    for row in range(nrows_orig):
        for col in range(ncols_orig):
            data_tiled[row][col] = data[row][col]
            data_tmp[0][row][col] = data[row][col]

    for i in range(1, n*2):

        for row in range(nrows_orig):
            for col in range(ncols_orig):
                val = (data_tmp[i-1][row][col] + 1) % 9
                if val == 0:
                    val = 9
                data_tmp[i][row][col] = val

    for j in range(n):
        for i in range(n):
            for row in range(nrows_orig):
                for col in range(ncols_orig):
                    data_tiled[row+nrows_orig*i][col+ncols_orig*j] = data_tmp[i+j][row][col]

    return data_tiled


def find_lowest_risk(data, dup=1):

    data = tile_data(data, dup)
    nrows, ncols = len(data), len(data[0])

    risk = {(i, j): float("inf") for i in range(nrows) for j in range(ncols)}
    queue = [(0, (0, 0))]

    while queue:
        current_risk, position = heapq.heappop(queue)

        for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighb = d[0] + position[0], d[1] + position[1]
            if neighb in risk:
                new_risk = current_risk + data[neighb[1]][neighb[0]]
                if new_risk < risk[neighb]:
                    risk[neighb] = new_risk
                    heapq.heappush(queue, (new_risk, neighb))

    return risk[(nrows-1, ncols-1)]


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    data = [[int(x) for x in row] for row in Path(args.infile).read_text().rstrip("\n").split("\n")]

    print(find_lowest_risk(data))
    print(find_lowest_risk(data, 5))
