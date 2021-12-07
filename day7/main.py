from argparse import ArgumentParser
from collections import Counter
from functools import partial
from pathlib import Path


def fuel_func1(x1, x2):
    return abs(x1 - x2)


def fuel_func2(x1, x2, fuel_map):
    return fuel_map[fuel_func1(x1, x2)]


def calc_fuel(positions, new_position, fuel_func):
    return sum(fuel_func(pos, new_position)*num for pos, num in positions.items())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    positions = Counter([int(x) for x in Path(args.infile).read_text().rstrip("\n").split(",")])

    start, end = min(positions.keys()), max(positions.keys())+1

    fuel_map = {0: 0}
    for x in range(1, end):
        fuel_map[x] = fuel_map[x-1]+x

    fuel_func_mapped = partial(fuel_func2, fuel_map=fuel_map)

    for f in fuel_func1, fuel_func_mapped:
        print(min(calc_fuel(positions, x, f) for x in range(start, end)))
