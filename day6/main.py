from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def calc_num_fish(fish, days):

    for _ in range(days):
        fish_new = Counter()
        for i in range(8, 0, -1):
            fish_new[i-1] = fish[i]

        fish_new[8] = fish[0]
        fish_new[6] += fish[0]
        fish = fish_new

    return sum(fish.values())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    fish = Counter([int(x) for x in Path(args.infile).read_text().rstrip("\n").split(",")])

    print(calc_num_fish(fish, 80))
    print(calc_num_fish(fish, 256))
