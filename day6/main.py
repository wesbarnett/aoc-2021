from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    fish = [int(x) for x in Path(args.infile).read_text().rstrip("\n").split(",")]

    days = 80

    for _ in range(days):
        fish_new = list(fish)
        for i, x in enumerate(fish):
            fish_new[i] -= 1
            if fish_new[i] == -1:
                fish_new[i] = 6
                fish_new.append(8)
        fish = list(fish_new)

    print(len(fish))
