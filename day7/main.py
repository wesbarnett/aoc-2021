from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def calc_fuel(positions, new_position):
    return sum(abs(pos - new_position)*num for pos, num in positions.items())


def calc_fuel_part2(positions, new_position):

    total_fuel = 0
    for pos, num in positions.items():
        fuel = sum(range(1, abs(pos - new_position)+1))
        total_fuel += fuel*num
    return total_fuel


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    positions = Counter([int(x) for x in Path(args.infile).read_text().rstrip("\n").split(",")])

    print(min(calc_fuel(positions, x) for x in range(min(positions.keys()), max(positions.keys())+1)))

    print(min(calc_fuel_part2(positions, x) for x in range(min(positions.keys()), max(positions.keys())+1)))
