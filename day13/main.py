from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def fold_horizontal(thermal_image, max_x, fold):
    for y in range(fold):
        for x in range(max_x):
            thermal_image[(x, fold-y)] += thermal_image[(x, fold+y)]
            if thermal_image[(x, fold-y)] > 0:
                thermal_image[(x, fold-y)] = 1
            thermal_image[(x, fold+y)] = 0


def fold_vertical(thermal_image, max_y, fold):
    for x in range(fold):
        for y in range(max_y):
            thermal_image[(fold-x, y)] += thermal_image[(fold+x, y)]
            if thermal_image[(fold-x, y)] > 0:
                thermal_image[(fold-x, y)] = 1
            thermal_image[(fold+x, y)] = 0


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    instructions = []
    thermal_image = Counter()
    max_x = 0
    max_y = 0
    for line in lines:
        if line.startswith("fold along"):
            instructions.append(line)
        elif line:
            x, y = line.split(",")
            x, y = int(x), int(y)
            thermal_image[(x, y)] = 1
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    print(thermal_image)
    for inst in instructions[:1]:
        _, val = inst.split("=")
        val = int(val)
        if "x" in inst:
            fold_vertical(thermal_image, max_y, val)
        elif "y" in inst:
            fold_horizontal(thermal_image, max_x, val)
        else:
            raise ValueError("Unknown fold instruction.")
    print(sum(thermal_image.values()))
